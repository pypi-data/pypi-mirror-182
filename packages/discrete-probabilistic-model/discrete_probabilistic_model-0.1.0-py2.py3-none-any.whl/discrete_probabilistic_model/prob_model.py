import numpy as np
from collections import defaultdict
import itertools
from .utils import sample_categorical, select


class ProbModel:
    """
    A simple Probabilistic Program framework for models with only discrete variables.
    Kind of based on WebPPL, except only enumeration-based inferences are possible.

    To define a model, create a new sub-class and implement forward().
        The final return value(s) of forward() must be hashable.
        For some simple items, use utils.misc.freeze().

    TODO:
        1. Implement inference using conditions and do-ops for getting conditional probabilities.
        2. Clean up categorical(); a lot of the shape-related things are really messy.

    Example usage:
        class Model(ProbModel):
            def forward(self):
                categories = np.array(list(string.ascii_uppercase[:24])).reshape(2, 4, 3)
                probs = np.array([[.1, .2, .3, .4],
                                  [.4, .2, .2, .2]])

                x = self.categorical('x', probs, categories, size=2)
                x = freeze(x)
                y = self.categorical('y', categories=['a', 'b', 'c'])
                return x, y

        model = Model()
        sample = model.sample()
        llh = model.get_likelihoods()
        len(llh)  # 768
    """

    def __init__(self, seed=None):
        self.rng = np.random.default_rng(seed)
        self.trace = {}  # variable_name -> (prob, value)
        self.last_traces = []  # store traces from last sample() call; it's just a feature, not really used for anything
        self.do = {}  # tracks do-operations during sampling
        self.enum_mode = False
        self.enum_trace = {}  # variable_name -> (prob, value)
        # similar to trace but used in get_likelihoods() since trace uses prob=1 for do-operations
        self.likelihoods = None

    @classmethod
    def get_model_posteriors(cls, models, observations, priors=None):
        """
        Returns the belief distribution for all models, starting from the priors to
        after all the observations.
        If priors is None, starts with a uniform distribution.
        return: array of shape [1 + len(observations), len(models)]
        """
        num_models = len(models)
        if priors is None:
            priors = np.ones(num_models) / num_models
        else:
            priors = np.array(priors)
        if len(priors) != num_models:
            raise Exception(f"Length of models {num_models} must match length of priors {len(priors)}")

        likelihoods = [model.get_likelihoods() for model in models]
        likelihoods, outcomes = _create_likelihood_matrix(likelihoods)
        outcome_indices = {o: i for i, o in enumerate(outcomes)}
        observations = np.array([outcome_indices[o] for o in observations])

        posteriors = [priors]
        for llh in likelihoods.T[observations]:
            p_oh = llh * posteriors[-1]
            denom = p_oh.sum()
            p_ho = p_oh / denom
            posteriors.append(p_ho)
        return np.array(posteriors)

    def forward(self):
        raise NotImplementedError

    def sample(self, num_samples=None, **kwargs):
        self.do = kwargs
        outcomes = []
        self.last_traces = []
        for i in range(1 if num_samples is None else num_samples):
            self.trace = {}
            outcome = self.forward()
            outcomes.append(outcome)
            self.last_traces.append(self.trace)

        if num_samples is None:
            self.last_traces = self.trace
            return outcome
        return outcomes

    def get_likelihoods(self, trace=False):
        """
        Returns a dict mapping outcomes to probabilities.
        Outcomes may be frozen.
        """
        if self.likelihoods is None:
            self.enum_mode = True
            self.enum_stack = [{}]
            self.enum_traces = defaultdict(list)
            likelihoods = defaultdict(int)
            while self.enum_stack:
                self.enum_trace = self.enum_stack.pop()
                do = {k: v[1] for k, v in self.enum_trace.items()}
                outcome = self.sample(**do)
                prob = np.prod([p for p, value in self.enum_trace.values()])
                likelihoods[outcome] += prob
                if trace:
                    self.enum_traces[outcome].append(self.enum_trace)
            self.enum_traces = dict(self.enum_traces)
            self.likelihoods = dict(likelihoods)
            self.enum_mode = False
        return self.likelihoods

    def categorical(self, name, probs=None, categories=None, size=None):
        """
        The returned categories may be converted into np.ndarray
        """
        if name in self.trace:
            raise Exception(f"Variable {name} already exists. Each variable must have a unique name.")
        if size is not None and np.prod(size) == 0:
            raise Exception("size cannot be 0")
        probs, categories = _format_categorical_args(probs, categories)  # sets default values

        if name in self.do:
            p_sample = 1
            sample = self.do[name]
        elif self.enum_mode:
            if size is None or np.issubdtype(type(size), np.integer):
                _size = (1 if size is None else size,)
            else:
                _size = size
            idx_shape = _size + probs.shape[:-1]

            num_samples = 1 if size is None else np.prod(_size)
            indices = itertools.product(
                *[range(probs.shape[-1])] * (np.prod(probs.shape[:-1], dtype=int) * num_samples))
            categories = np.broadcast_to(categories, _size + categories.shape)
            probs = np.broadcast_to(probs, _size + probs.shape)

            for i, idx in enumerate(indices):
                idx = np.array(idx).reshape(idx_shape)
                _sample = select(categories, idx)
                if size is None:
                    _sample = _sample.squeeze(0)
                    if len(_sample.shape) == 0:
                        _sample = _sample.item()
                _p_sample = select(probs, idx).prod()

                if i == 0:
                    sample = _sample
                    p_sample = _p_sample
                else:
                    trace = self.enum_trace.copy()
                    trace[name] = (_p_sample, _sample)
                    self.enum_stack.append(trace)
            self.enum_trace[name] = (p_sample, sample)
        else:
            sample, p_sample = sample_categorical(probs, categories=categories, size=size, return_probs=True,
                                                  rng=self.rng)
            p_sample = p_sample.prod()

        self.trace[name] = (p_sample, sample)
        return sample

    def bernoulli(self, name, probs=.5, size=None):
        if not isinstance(probs, np.ndarray):
            probs = np.array(probs)
        probs = np.stack([1 - probs, probs], axis=-1)
        return self.categorical(name, probs=probs, size=size).astype(bool)


def _create_likelihood_matrix(likelihood_dicts: list):
    """
    Converts a list of likelihood_dicts into a numpy.ndarray
    """
    outcomes = list(set.union(*[set(l) for l in likelihood_dicts]))
    likelihoods = np.zeros((len(likelihood_dicts), len(outcomes)))
    for i, llh in enumerate(likelihood_dicts):
        for j, o in enumerate(outcomes):
            likelihoods[i, j] = 0 if o not in llh else llh[o]
    return likelihoods, outcomes


def _format_categorical_args(probs, categories):
    if probs is None and categories is None:
        raise Exception(f"Either probs or categories must be defined for categorical variables.")
    if probs is not None and not isinstance(probs, np.ndarray):
        probs = np.array(probs)
    if categories is not None and not isinstance(categories, np.ndarray):
        categories = np.array(categories)

    if probs is None:
        probs = np.full(categories.shape, 1 / categories.shape[-1])
    if categories is None:
        categories = np.broadcast_to(np.arange(probs.shape[-1]), probs.shape)

    if categories.size == 0:
        raise Exception(f"Empty arrays. Check probs {probs.shape} and categories {categories.shape}")
    return probs, categories

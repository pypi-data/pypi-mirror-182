import numpy as np
from frozendict import frozendict


class FrozenArray(np.ndarray):
    """
    Upon clashing hash values, will throw
        ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    If a clash happens, try setting FrozenArray.HASHKEY to something else.
    This will change the resulting hash values, which might avoid the clash.
    If clashes happen because there are too many entries in a dict, *shrug*
    """
    HASHKEY = 0

    @classmethod
    def freeze(cls, a):
        b = FrozenArray(a.shape, dtype=a.dtype)
        b[...] = a[...]
        b.flags.writeable = False
        b._hash = None
        return b

    def __hash__(self):
        if self._hash is None:
            self._hash = hash((self.dtype, self.shape, self.tobytes()))
        return self._hash


def freeze(x):
    """
    Turns a typically unhashable object into a hashable one.
    If the object is not one of the types covered in the function, returns the object itself.
    :param x:
    :return:
    """
    if isinstance(x, np.ndarray):
        return FrozenArray.freeze(x)
    if isinstance(x, list):
        return tuple(x)
    if isinstance(x, dict):
        return frozendict(x)
    if isinstance(x, set):
        return frozenset(x)
    return x


def select(array, indices):
    """
    Given an array and indices where the shape of indices is the same as the start of array's shape
    returns an array of shape [...] where each index in indices selects from array at its corresponding location.
    Can also select submatrices.
    >>> a = np.arange(3*4*5).reshape((3, 4, 5))
    >>> x = np.array([[1, 2, 3, 4], [0, 3, 2, 1], [4, 1, 2, 1]])
    >>> select(a, x)
    array([[ 1,  7, 13, 19],
           [20, 28, 32, 36],
           [44, 46, 52, 56]])
    >>> a = np.arange(2*3*4*2).reshape(2, 3, 4, 2)
    >>> idx = np.array([[2, 1, 0], [2, 1, 2]])
    >>> select(a, idx)
    array([[[ 4,  5],
            [10, 11],
            [16, 17]],

           [[28, 29],
            [34, 35],
            [44, 45]]])
    """
    if len(indices.shape) == 0:
        return array[indices]

    index_shape = indices.shape
    selected_shape = array.shape[len(index_shape):]
    indices = indices.flatten()
    array = array.reshape(len(indices), *selected_shape)
    selected = array[range(len(indices)), indices]
    return selected.reshape(*(index_shape + selected_shape[1:]))


def sample_categorical(probs, categories=None, size=None, return_probs=False, rng=None):
    """
    Similar to rng.choice, but probs and categories can be multi-dimensional.
    If return_probs is True, also returns the probabilities of the individual samples.

    >>> probs = np.array([[.1, .2, .3, .4], [.4, .2, .2, .2]])
    >>> categories = np.arange(2*4*3).reshape(2, 4, 3)
    >>> samples = sample_categorical(rng, probs, categories, (5, 6))
    >>> print(samples.shape)
    (5, 6, 2, 3)
    """
    if rng is None:
        rng = np.random.default_rng()

    if size is None:
        indices = rng.multinomial(1, probs).argmax(-1)
    else:
        size = (size,) if np.issubdtype(type(size), np.integer) else tuple(size)
        indices = rng.multinomial(1, probs, size + probs.shape[:-1]).argmax(-1)

    if return_probs:
        if size is not None:
            probs = np.broadcast_to(probs, size + probs.shape)
        probs = select(probs, indices)

    if categories is None:
        return (indices, probs) if return_probs else indices
    if size is not None:
        categories = np.broadcast_to(categories, size + categories.shape)
    samples = select(categories, indices)
    return (samples, probs) if return_probs else samples

#!/usr/bin/env python

"""Tests for `discrete_probabilistic_model` package."""


import unittest
import numpy as np
import string
from discrete_probabilistic_model import ProbModel
from discrete_probabilistic_model.utils import freeze


class TestDiscrete_probabilistic_model(unittest.TestCase):
    """Tests for `discrete_probabilistic_model` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_simple_model(self):
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
        llh = model.get_likelihoods()
        self.assertAlmostEqual(sum(llh.values()), 1)
        self.assertEqual(len(llh), 768)


if __name__ == '__main__':
    unittest.main()

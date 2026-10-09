import numpy as np


def test_numpy_array():
    x = np.array([1.0, 2.0, 3.0])

    assert x.shape == (3,)
    assert np.sum(x) == 6.0

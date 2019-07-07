import pytest
import my_module

import numpy as np

@pytest.fixture(scope='session') # this fixture is used for the whole test session
def multiplier7():
    return my_module.Multiplier(7)

@pytest.fixture # default is to create a fixture object for every test function
def vals_for_test():
    vals = np.random.randn(20)
    expectations = vals*2
    return vals, expectations

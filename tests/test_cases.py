import pytest
import my_module
import utils

def test_double_1():
    """simple test case"""
    assert my_module.double_me(1) == 2 # asserts are used in pytest to check expectations
    
    # you can put multiple asserts into one test function, but it is still considered as a single test case
    assert my_module.double_me(-5) == -10 

def test_which_fails():
    """test case which always fails 
    - just for illustration here, do not put something like this in real test cases!"""
    assert my_module.double_me(1) == 3

def test_error_message():
    """checks raising of error"""
    with pytest.raises(TypeError):
        assert my_module.double_me({1, 2, 3})

@pytest.mark.parametrize('input, expected', [(2, 4), (3, 6), (4, 8)])
def test_double_2(input, expected):
    """testing multiple inputs with corresponding expected outputs"""
    assert my_module.double_me(input) == expected
    
def test_double_3(vals_for_test):
    """using pytest.fixture for defining test values and expected outputs"""
    vals, expectations = vals_for_test
    assert (expectations == my_module.double_me(vals)).all()
    # same as above, but using defined utility function
    assert utils.compare_np_arrays(expectations, my_module.double_me(vals))
    
def test_multiplier(multiplier7):
    """using pytest.fixture for construction of test objects"""
    assert multiplier7.get_result(3) == 21

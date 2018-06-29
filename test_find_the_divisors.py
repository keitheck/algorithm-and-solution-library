from find_the_divisors import divisors as div 
import pytest


def test_input():
    """
    Test (float) that TypeError is raised when non-integer argument used.
    """
    with pytest.raises(TypeError):
        div(3.5)


def test_input_two():
    """
    Test (iterable) that TypeError is raised when non-integer argument used.
    """
    with pytest.raises(TypeError):
        div([1, 2, 3, 4])


def test_results_one():
    """
    Test return as expected.
    """
    assert div(1) == '1 is prime'


def test_results_two():
    """
    Test return as expected.
    """
    assert div(6) == [2, 3]


def test_results_three():
    """
    Test return as expected.
    """
    assert div(39) == [3, 13]
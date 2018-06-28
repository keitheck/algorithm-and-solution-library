from return_n_occurances_of_list_elements import delete_nth
import pytest


def test_data_type():
    """tests typeerror handled correctly"""
    with pytest.raises(TypeError):
        delete_nth({'IamAstring': 99}, 2)


@pytest.fixture
def short_arr():
    """returns list for testing."""
    return [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


@pytest.fixture
def long_arr():
    """returns list for testing."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 1, 105, 556, 1, 2, 3, 4,
            3, 3, 3, 1, 2, 3, 4]


def test_one(short_arr):
    """test returns as expected"""
    assert delete_nth(short_arr, 1) == [1, 2, 3, 4]


def test_two(short_arr):
    """test returns as expected"""
    assert delete_nth(short_arr, 2) == [1, 2, 3, 4, 1, 2, 3, 4]


def test_three(short_arr):
    """test returns as expected"""
    assert delete_nth(short_arr, 3) == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


def test_four(short_arr):
    """test returns as expected"""
    assert delete_nth(short_arr, 5) == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1,
                                        2, 3, 4, 1, 2, 3, 4]


def test_five(long_arr):
    """test returns as expected"""
    assert delete_nth(long_arr, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 105, 556]


def test_six(long_arr):
    """test returns as expected"""
    assert delete_nth(long_arr, 3) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3,
                                       4, 1, 105, 556, 2, 3, 4]


def test_seven(long_arr):
    """test returns as expected"""
    assert delete_nth(long_arr, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3,
                                         4, 1, 105, 556, 1, 2, 3, 4, 3, 3, 3,
                                         1, 2, 3, 4]


def test_eight():
    """test if touple functions as expected"""
    assert delete_nth((1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5), 3) == [1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5]


def test_nine():
    """tests float values return as expected"""
    assert delete_nth([1, 1.5, 2, 9.999, 1.5, 9.999, 1.5], 2) == [1, 1.5, 2, 9.999, 1.5, 9.999]


def test_ten():
    """test non-integer/float indexes are error handled"""
    with pytest.raises(TypeError):
        delete_nth([1, 2, 3, 4.776, 1, 2, 3, 4, 'car', 2, 3, 4], 3)
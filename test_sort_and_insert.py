import pytest
from sort_and_insert import sort_insert as si 


def test_sorted():
    """Test function returns list as expected."""
    assert si(
        ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
        ) == 'b***i***t***c***o***i***n'


def test_other_iterable_one():
    """Test function returns list as expected."""
    assert si(
        ('bobcat', 'zebra', 'gnu', 'tiger', 'ardvark')
        ) == 'a***r***d***v***a***r***k'


@pytest.fixture
def list_ints():
    """Returns unordered list of ints."""
    return [6, 9, 4, 2, 8]


def test_list_of_ints():
    """Error handling."""
    with pytest.raises(TypeError):
        si(list_ints)


@pytest.fixture
def dictionary():
    """Returns dictionary."""
    return {'g': 4, 'y': 9, 't': 5, 'a': 1}


def test_other_iterable_two():
    """Error Handling."""
    with pytest.raises(TypeError):
        si(dictionary)

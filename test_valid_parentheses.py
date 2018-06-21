import pytest
from valid_parentheses import valid_parentheses

@pytest.fixture
def small_false():
    return '([]lkd)('


@pytest.fixture
def medium_false():
    return '([]lkd)(c))))'


@pytest.fixture
def long_true():
    return 'dr^#s(gg[s]lkd)(l><<])()((fde0)56)'


@pytest.fixture
def small_no_paren():
    return 'hfgb[]lkd;ly78'


def test_typeerror():
    """Test TypeError Exception properly handled"""
    with pytest.raises(TypeError):
        valid_parentheses(1234)


def test_typerror_2(): 
    """Test TypeError Exception properly handled"""
    with pytest.raises(TypeError):
        valid_parentheses({'teststring': 'testvalue'})


def test_one(small_false):
    """Tests string returns False"""
    assert valid_parentheses(small_false) is False


def test_two(long_true):
    """Tests string returns True"""
    assert valid_parentheses(long_true) is True


def test_three(small_no_paren):
    """Tests no parentheses in string returns True"""
    assert valid_parentheses(small_no_paren) is True


def test_four(medium_false):
    """Tests no parentheses in string returns True"""
    assert valid_parentheses(medium_false) is False


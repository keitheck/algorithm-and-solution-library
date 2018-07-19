import pytest
from odd_or_even_1 import odd_or_even as oe 


def test_odd():
    """Simple test that odd integer returns as expected"""
    assert oe(3) == 'odd'


def test_even():
    """Simple test that odd integer returns as expected"""
    assert oe(8) == 'even'


def test_odd_lg():
    """Simple test that odd integer returns as expected"""
    assert oe(7449573339507) == 'odd'


def test_even_lg():
    """Simple test that odd integer returns as expected"""
    assert oe(793764662290048566388296) == 'even'


def test_error_handling():
    """Tests Error handled when non-integer argument used"""
    with pytest.raises(TypeError):
        oe(3.4)


def test_error_handling():
    """Tests Error handled when non-integer argument used"""
    with pytest.raises(TypeError):
        oe('99')

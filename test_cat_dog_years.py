from cat_dog_years import human_years_cat_years_dog_years as hcd
import pytest


def test_type_string():
    with pytest.raises(TypeError):
        hcd('18')


def test_type_arr():
    with pytest.raises(TypeError):
        hcd([18])


def test_type_dict():
    with pytest.raises(TypeError):
        hcd({'years': 18, 'animal': 'dog'})


def test_expected_output_one():
    assert hcd(1) == [1,15,15]


def test_expected_output_two():
    assert hcd(2) == [2, 24, 24]


def test_expected_output_three():
    assert hcd(3) == [3, 28, 29]


def test_expected_output_large():
    assert hcd(145) == [145, 596, 739]

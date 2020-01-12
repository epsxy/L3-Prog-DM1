import pytest

from ex2.core import compute_weighted_avg


def test_should_raise_an_exception_if_numbers_list_has_not_len_10():
    with pytest.raises(Exception):
        assert compute_weighted_avg(
            [1, 2, 3],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def test_should_raise_an_exception_if_coeff_list_has_not_len_10():
    with pytest.raises(Exception):
        assert compute_weighted_avg(
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [1, 2, 3])


def test_should_compute_nominal_weighted_avg():
    avg = compute_weighted_avg(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    assert avg == 10


def test_should_compute_complex_weighted_avg():
    avg = compute_weighted_avg(
        [10, 5, 12, 7, 9, 1, 3, 5, 14, 18],
        [1, 1, 3, 1, 6, 1, 1, 3, 1, 6])

    assert round(avg*100)/100 == 10.54


def test_should_compute_nominal_weighted_avg():
    with pytest.raises(TypeError):
        assert compute_weighted_avg(
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

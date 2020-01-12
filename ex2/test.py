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


def test_should_compute_nominal_weighted_avg():
    with pytest.raises(TypeError):
        assert compute_weighted_avg(
            ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

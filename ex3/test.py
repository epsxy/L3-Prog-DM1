from ex3.core import find_all_divisors, find_perfect_numbers_below_999


def test_should_find_all_divisors_of_a_number():
    res = find_all_divisors(6)

    assert res == [1, 2, 3]


def test_should_find_one_trivial_divisor_if_number_is_prime():
    res = find_all_divisors(7)

    assert res == [1]


def test_should_find_perfect_numbers_below_999():
    res = find_perfect_numbers_below_999()

    assert len(res) == 3
    assert (6, [1, 2, 3]) in res
    assert (28, [1, 2, 4, 7, 14]) in res
    assert (496, [1, 2, 4, 8, 16, 31, 62, 124, 248]) in res

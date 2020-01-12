from ex1.core import sum_for_computing_pi, \
    compute_error_for_current_idx, \
    get_pi_from_sum, \
    compute_pi


def test_should_compute_pi_sum_for_n_equals_3():
    res = sum_for_computing_pi(3)

    assert round(res * 100000) / 100000 == 1.36111


def test_should_compute_pi_sum_for_n_equals_10():
    res = sum_for_computing_pi(10)

    assert round(res * 10000000) / 10000000 == 1.5497677


def test_should_compute_error_for_idx_10():
    res = compute_error_for_current_idx(10)

    assert round(res * 100) / 100 == 0.01


def test_should_get_pi_from_sum():
    res = get_pi_from_sum(1.5497677)

    assert round(res * 10000000) / 10000000 == 3.0493616


def test_should_get_other_pi_from_sum():
    res = get_pi_from_sum(1.6436848477727068)

    assert round(res * 10000000) / 10000000 == 3.1403995


def test_compute_pi():
    res = compute_pi(0.000001)

    assert round(res * 100000) / 100000 == 3.14064

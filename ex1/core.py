from math import sqrt


# Memoize function used to store in memory previous recursion results
def memoize(func):
    cache = dict()

    def inner_func(num):
        if num not in cache:
            cache[num] = func(num)
        return cache[num]

    return inner_func


@memoize
def sum_for_computing_pi(n: int) -> float:
    if n == 1:
        return 1
    return (1 / pow(n, 2)) + sum_for_computing_pi(n - 1)


def compute_error_for_current_idx(error_idx: int) -> float:
    if error_idx < 2:
        raise Exception("sum not defined for idx < 1")
    return abs(sum_for_computing_pi(error_idx) - sum_for_computing_pi(error_idx - 1))


def get_pi_from_sum(sum_for_pi: float) -> float:
    return sqrt(6 * sum_for_pi)


def compute_pi(precision: float) -> float:
    idx = 2
    error = compute_error_for_current_idx(idx)
    while error > precision:
        idx += 1
        error = compute_error_for_current_idx(idx)
    return get_pi_from_sum(sum_for_computing_pi(idx))

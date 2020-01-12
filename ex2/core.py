from typing import List


def compute_weighted_avg(numbers: List[float], coefficients: List[float]) -> float:
    if len(numbers) != 10:
        print('numbers: {}'.format(numbers))
        raise Exception('numbers must be of size 10. size is {}'.format(len(numbers)))
    if len(coefficients) != 10:
        print('coefficients: {}'.format(numbers))
        raise Exception('coefficients must be of size 10. size is {}'.format(len(coefficients)))
    sum_numbers = 0.0
    for (number, coeff) in zip(numbers, coefficients):
        sum_numbers += number * coeff
    return sum_numbers / sum(coefficients)
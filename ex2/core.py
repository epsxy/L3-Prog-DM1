from typing import List


def compute_weighted_avg(numbers: List[float], coefficients: List[float]) -> float:
    if len(numbers) != 10:
        template_str = 'numbers must be of size 10. size is {}'
        raise Exception(template_str.format(len(numbers)))
    if len(coefficients) != 10:
        template_str = 'coefficients must be of size 10. size is {}'
        raise Exception(template_str.format(len(coefficients)))
    sum_numbers = 0.0
    for (number, coeff) in zip(numbers, coefficients):
        sum_numbers += number * coeff
    return sum_numbers / sum(coefficients)

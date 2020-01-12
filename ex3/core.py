from typing import List, Tuple


def find_all_divisors(number: int) -> List[int]:
    divisors_list = []
    index = 1
    while index < number:
        if number % index == 0:
            divisors_list.append(index)
        index += 1
    return divisors_list


def find_perfect_numbers_below_999() -> List[Tuple[int, List[int]]]:
    index = 2
    result = []
    while index < 1000:
        if sum(find_all_divisors(index)) == index:
            result.append((index, find_all_divisors(index)))
        index += 1
    return result
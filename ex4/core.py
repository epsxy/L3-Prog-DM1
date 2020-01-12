import string
from typing import List


def str_compare_char(first_str: string, second_str: string) -> List[int]:
    chars = []
    for (first_char, second_char) in zip(first_str, second_str):
        if first_char == second_char:
            chars.append(first_char)
    return chars

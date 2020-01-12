from ex3.core import find_perfect_numbers_below_999

if __name__ == '__main__':
    perfect_numbers = find_perfect_numbers_below_999()
    str_template = '{} is perfect, its divisors are: {}'

    for (idx, divs) in perfect_numbers:
        print(str_template.format(idx, divs))

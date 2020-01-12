from ex2.core import compute_weighted_avg

if __name__ == '__main__':
    input_str = 'please enter 10 real comma-separated {} (e.g.: 1,2,3,4,5,6,7,8,9,10): '
    user_number_input = input(input_str.format('numbers')).split(',')
    user_coefficient_input = input(input_str.format('coefficients')).split(',')
    print(compute_weighted_avg(
        list(map(lambda nb: float(nb), user_number_input)),
        list(map(lambda nb: float(nb), user_coefficient_input))
    ))

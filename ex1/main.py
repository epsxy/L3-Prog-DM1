from ex1.core import compute_pi

if __name__ == '__main__':
    precision_str = input('enter epsilon value for sum computation (e.g. 0.01): ')
    res = compute_pi(float(precision_str))
    print('computed pi value is: {}'.format(res))

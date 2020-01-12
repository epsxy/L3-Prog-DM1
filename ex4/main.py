from ex4.core import str_compare_char

if __name__ == '__main__':
    str_one = input('enter first string: ')
    str_two = input('enter second string: ')

    chars_list = str_compare_char(str_one, str_two)

    str_template = '{} characters in common were found. These characters are {}'
    print(str_template.format(len(chars_list), chars_list))

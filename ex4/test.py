from ex4.core import str_compare_char


def test_should_compare_with_exact_match():
    res = str_compare_char('hey', 'hey')

    assert res == ['h', 'e', 'y']


def test_should_compare_with_no_match():
    res = str_compare_char('hey', '今日は')

    assert res == []


def test_should_compare_different_str_length_with_first_smaller():
    res = str_compare_char('hey', 'hey jude')

    assert res == ['h', 'e', 'y']


def test_should_compare_different_str_length_with_first_bigger():
    res = str_compare_char('hey jude', 'hey')

    assert res == ['h', 'e', 'y']


def test_should_compare_with_partial_match():
    res = str_compare_char('hey jude', 'hey jade, how are you?')

    assert res == ['h', 'e', 'y', ' ', 'j', 'd', 'e']

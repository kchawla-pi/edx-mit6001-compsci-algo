def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception.
          For example, sum_digits("a;35d4") returns 12. """
    string_sum = [int(char_) for char_ in s if char_.isdigit()]
    if string_sum:
        return sum(string_sum)
    else:
        raise ValueError
        # return None
def test_sum_digits():
    test_data = {
        "a;35d4" : 12,
        "n3oirj98fua8j98u09y(*&(&joirnoi4noifnanmgoi690": 73,
    "  (*&*(BBBytfytfytf%^%$8768763009hnfoin8y29y0939ur-9gu97y   47yf7 fw89ur04u0t9 v0 ": 167,
        '': None,
        ' ': None,
        '0jioj0': 0,
        'wvwvergreFEGW$%%#Q%': None,
        }
    results = [sum_digits(test_) == expected for test_, expected in test_data.items()]
    print(results)
    print(sum(results))
    assert sum(results) == len(results)

test_sum_digits()

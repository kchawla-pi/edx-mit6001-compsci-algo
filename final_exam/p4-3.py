def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    print(t)
    first, *rest = t
    try:
        new_t = [*rest, max(first)]
    except TypeError:
        new_t = [*rest, first]
    try:
        sum(new_t)
    except TypeError:
        max_num = max_val(new_t)
    else:
        return max(new_t)
    return max_num
    
    


def create_test_data():
    test_data = {
        0: (9, (1, 2), [[1], [5]]),
        1: (5, (1, 2), [[1], [2]]),
        2: ([0, -5], (1, 2), [[1], [2]]),
        3: ([0, -5], (1, 2), [[1], [2]], 7),
        4: [[[[[[6]]]]]],
        5: [[[[[[6, 7]]]]]],
        6: [[[[[[6]]], 5]]],
        }
    expected = {
        0: 9,
        1: 5,
        2: 2,
        3: 7,
        4: 6,
        5: 7,
        6: 6,
        }
    return test_data, expected


def test_max_val():
    test_data, expected = create_test_data()
    for key in test_data:
        actual = max_val(test_data[key])
        print('actual: {}\nexpected: {}'.format(actual, expected[key]))
        # assert actual == expected[key], actual


# test_max_val()

# t = max_val([[[[[[6]]]]]])
# print(t)
# t = max_val((5, (1, 2), [[1], [9]]))
# print(t)

t= max_val([[[[[[6]]], 5]]])
print(t)


    # print(t)
    # t = list(t)
    # try:
    #     print(t)
    #     t_last = t.pop()
    # except TypeError:
    #
    #     try:
    #         t_last = max(t_last)
    #     except TypeError:
    #         pass
    #     else:
    #         returned_val = max_val(t)
    # else:
    #     return returned_val
    # # max(max_val(t)
    # max(
    # if t_last
    # try:
    #     t_last = t.pop()
    # except TypeError:
    #     return t
    # else:
    #     curr_max = max(t_last)
    #     val_returned = max_val(t)
    #     return max(curr_max, val_returned)
    #

def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    try:
        t_len = len(t)
    except TypeError:
        return t
    else:
        if t_len == 1:
            t = max_val(t[0])
            return t
        
        t = [*t]
        popped = t.pop()
        
        # try:
        #     popped = t.pop()
        # except AttributeError:
        #     t = list(t)
        #     popped = t.pop()
    
        try:
            t.extend(popped)
        except TypeError:
            t.insert(0, popped)
        try:
            return max(t)
        except TypeError:
            return max_val(t)
    
    
def create_test_data():
    test_data = {
        0: (5, (1, 2), [[1], [9]]),
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
        assert actual == expected[key]
    

test_max_val()

t = max_val([[[[[[6]]]]]])
print(t)
t = max_val((5, (1,2), [[1],[9]]))
print(t)

# t = list(t)
# popped = t.pop()
# try:
#     max_popped = max(popped)
# except TypeError:
#     t.insert(0, popped)
# else:
#     t.insert(0, max_popped)
#
# return max_val(t)

# t = list(t)
# try:
#     t[-1] = max(t[-1])
# except TypeError:
#     return max(t[-1], max_val(t[:-1]))
# except IndexError:
#     return NaN
# else:
#     return max_val(t)

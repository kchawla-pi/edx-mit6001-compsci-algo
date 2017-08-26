def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    try:
        sum(t)
    except TypeError:
        
        max_val()


def test_max_val():
    assert max_val((5, (1, 2), [[1], [9]])) == 9
    assert max_val((5, (1, 2), [[1], [2]])) == 5
    assert max_val(([0, -5], (1, 2), [[1], [2]])) == 2
    assert max_val(([0, -5], (1, 2), [[1], [2]], 7)) == 7
    assert max_val([[[[[[6]]]]]]) == 6


# test_max_val()
if __name__ == '__main__':
    t = max_val((5, (1, 2), [[1], [9]]))
    print(t)
    t = max_val([[[[[[6]]]]]])
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

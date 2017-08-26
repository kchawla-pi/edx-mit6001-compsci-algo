"""
 Write a Python function that takes in two lists and calculates whether they are permutations of each other.
 The lists can contain both integers and strings. We define a permutation as follows:

    the lists have the same number of elements
    list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, the function returns a tuple consisting of the following elements:

    the element occuring the most times
    how many times that element occurs
    the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.

For example,

    if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
    if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then
        is_list_permutation returns (1, 3, <class 'int'>) because
        the integer 1 occurs the most, 3 times, and the type of 1 is an integer
        (note that the third element in the tuple is not a string).
"""


def test_fn(test_cases, fn, printIt=True):
    from pprint import pprint
    test_returns = {case_: fn(test_cases[case_][0], printIt=False) for case_ in test_cases}
    msg = "\n{}. \nIn: {}, \nReturned: {}, \nExpected: {}"
    msg_args = {case_: (test_cases[case_][0], test_returns[case_], test_cases[case_][1]) for case_
                in test_cases}
    test_results = [
        msg.format('Passed', *msg_args[case_]) if test_returns[case_] == test_cases[case_][1]
        else msg.format('Failed', *msg_args[case_]) for case_ in test_cases
        ]
    if printIt:
        for test_result_ in test_results:
            print('\n', test_result_)
    else:
        return test_results


def test_is_list_permutation(test_cases):
    for case_key, case_vals in test_cases.items():
        case_result = is_list_permutation(*case_vals[0:-1])
        print('\nPassed', '\nIn:', *case_vals[0: -1], '\nExpected:', case_vals[-1], '\nReturned:', case_result) if case_result == case_vals[-1] \
            else ('Failed', 'In:', *case_vals[0: -1], 'Expected:', case_vals[-1], 'Returned:', case_result)


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if not L1 and not L2:
        return None, None, None
    if len(L1) != len(L2):
        return False
    D1 = {elem: L1.count(elem) for elem in set(L1)}
    D2 = {elem: L2.count(elem) for elem in set(L2)}
    if D1 != D2:
        return False
    return next((k, v, type(k)) for k, v in D1.items() if max(D1.values()) == v)
    

if __name__ == '__main__':
    test_cases = {1: (['a', 'a', 'b'], ['a', 'b'], False),
                  2: ([1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c'], (1, 3, type(1)))
                  }
    test_is_list_permutation(test_cases)



"""
Write a function called dict_invert that takes in a dictionary with immutable values and returns
the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are
the unique dictionary values in d. The value for a key in the inverse dictionary is
a sorted list (increasing order) of all keys in d that have the same value in d.

Here are two examples:

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""


def test_fn(test_cases, fn, printIt=True):
    from pprint import pprint
    msg = "\n{}. \nIn: {}, \nReturned: {}, \nExpected: {}"
    test_results = [msg.format('Passed',
                               test_cases[case_][0],
                               fn(test_cases[case_][0], printIt=False),
                               test_cases[case_][1])
                    if fn(test_cases[case_][0], printIt=False) ==
                       test_cases[case_][1] else
                    msg.format('Change code',
                               test_cases[case_][0],
                               fn(test_cases[case_][0], printIt=False),
                               test_cases[case_][1])
                    for case_ in test_cases
                    ]
    if printIt:
        for test_num_, test_result_ in enumerate(test_results):
            print('\n', test_num_, test_result_)
    else:
        return test_results


def dict_invert(d, printIt=False):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    new_dict = dict.fromkeys(set(d.values()), list())
    for nkey in new_dict:
        new_dict[nkey] = sorted([k for k,v in d.items() if v == nkey])
    return new_dict

    try:
        result
    except NameError:
        result = None
    try:
        printIt
    except NameError:
        printIt = True
    if printIt:
        print(result)
        return None
    else:
        return result


if __name__ == '__main__':
    test_cases = {1: ({1: 10, 2: 20, 3: 30}, {10: [1], 20: [2], 30: [3]}),
                  2: ({1: 10, 2: 20, 3: 30, 4: 30}, {10: [1], 20: [2], 30: [3, 4]}),
                  3: ({4: True, 2: True, 0: True}, {True: [0, 2, 4]}),
                  4: ({(1, 2): 'a', (2, 3): 'b', (4, 3): 'a'}, {'a': [(1, 2), (4, 3)], 'b': [(2, 3)]}),
                  5: ({(1, 2): (True, True), (2, 3): (True, False), (3, 4): (False, True), (4, 5): (True, True)},
                      {(True, True): [(1, 2), (4, 5)], (True, False): [(2 ,3)], (False, True): [(3, 4)]})
                  }
    # test_cases = {1: test_cases[1]}
    test_fn(test_cases=test_cases, fn=dict_invert, printIt=True)


"""
Write a function that satisfies the following docstring:
Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None

For example, if

    largest_odd_times([2,2,4,4]) returns None
    largest_odd_times([3,9,5,3,5,3]) returns 9
"""


def test_fn(test_cases, fn, printIt=True):
    from pprint import pprint
    msg = "{}. In: {}, Returned: {}, Expected: {}"
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
        pprint(test_results)
    else:
        return test_results


def result_handler(result, printIt):
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


def largest_odd_times(L, printIt=False):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    """
    counts = {num: L.count(num) for num in set(L)}
    try:
        result = max([num for num in counts if counts[num] % 2 != 0])
    except ValueError:
        result = None
    return result_handler(result, printIt=printIt)
    
    
if __name__ == '__main__':
    test_cases = {1: ([2, 2, 4, 4], None),
                  2: ([3, 9, 5, 3, 5, 3], 9),
                  3: ([9, 9, 9, 9, 4, 5, 5, 1], 4),
                  4: ([-13, 3, 2, 1, 0], 3),
                  5: ([-13, -45, -2, -2, -1], -1),
                  6: ([-13, -45, -2, -2, -1, 0, 2, 2], 0),
                  7: ([9, 9, 9, 8, 8, 8, 7, 7, 7], 9),
                  8: ([9, 9, 9, 9, 8, 8, 8, 7, 7, 7], 8),
                  9: ([9, 9, 9, 9, 8, 8, 7, 7, 7], 7),
                  10: ([10, 9, 9, 9, 8, 8, 8, 7, 7, 7], 10),
                  11: ([10, 10, 10, 10], None),
                  12: ([10, 10, 10, 10, 10], 10)
                  }
    test_fn(test_cases=test_cases, fn=largest_odd_times, printIt=True)
    

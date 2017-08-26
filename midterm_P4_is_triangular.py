"""

Write a function is_triangular that meets the specification below. A triangular number is a number
obtained by the continued summation of integers starting from 1.
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc.,
are triangular numbers.

def is_triangular(k):

    # k, a positive integer
    # returns True if k is triangular and False if not
"""



def test_is_triangular(test_cases):
    # msg = "{}, ArgIn: {}, Value-- Returned: {}, Value-- Expected: {}, Bool-- Returned: {}, Bool-- Expected: {}"
    
    results = [('Passed.', case_, 'is_triangular is True, gave True') if is_triangular(case_) is True
               else ('Change Code.', case_, 'is_triangular is True, gave False')
               for case_ in test_cases[True]
               ]
    results.extend([('Passed.', case_, 'is_triangular is False, gave False')
                    if is_triangular(case_) is False
                    else ('Change Code.', case_, 'is_triangular is False, gave True')
                    for case_ in test_cases[False]
                    ]
                   )
    return results


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    total = 0
    num = 1
    while total < k:
        total += num
        num += 1
    return total == k


if __name__ == '__main__':
    from pprint import pprint
    test_cases = {True: (1, 3, 6, 10),
                  False:  (2, 11)
                  }
    for case_ in test_cases[True]:
        print(is_triangular(case_))
    print()
    for case_ in test_cases[False]:
        print(is_triangular(case_))
    pprint(test_is_triangular(test_cases))

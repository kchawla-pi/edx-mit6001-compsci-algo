"""
Write a function called general_poly, that meets the specifications below.
For example,
general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1*10^3+2*10^2+3*10^1+4*10^0.

If you are getting "exception thrown", you should read the specification CAREFULLY for what you need to return.
"""


def test_fn(test_cases, fn, printIt=True):
    from pprint import pprint
    test_returns = {case_: fn(test_cases[case_][0], printIt=False) for case_ in test_cases}
    msg = "\n{}. \nIn: {}, \nReturned: {}, \nExpected: {}"
    msg_args = {case_: (test_cases[case_][0], test_returns[case_], test_cases[case_][1]) for case_ in test_cases}
    test_results = [msg.format('Passed', *msg_args[case_]) if test_returns[case_] == test_cases[case_][1]
                    else msg.format('Failed', *msg_args[case_]) for case_ in test_cases
                    ]
    if printIt:
        for test_result_ in test_results:
            print('\n', test_result_)
    else:
        return test_results


def general_poly(L, printIt=False):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    # x = 10
    def __general_poly__(x):
        return  sum([L[idx] * x ** exp for idx, exp in enumerate(range(len(L)-1, -1, -1))])
    return __general_poly__


if __name__ == '__main__':
    test_cases = {1: ([1, 2, 3, 4], 1234)}
    gen_poly = general_poly(test_cases[1][0])
    print(gen_poly(10))
    print(general_poly(test_cases[1][0])(10))
    test_fn(test_cases=test_cases, fn=general_poly, printIt=True)

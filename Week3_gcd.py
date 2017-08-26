def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == a or b == 0:
        return a
    elif a == 0:
        return b
    potential_gcd = b if b < a else a
    while (b % potential_gcd != 0) or (a % potential_gcd != 0):
        potential_gcd -= 1
    return potential_gcd

tests = [(0, 34, 34), (23, 0, 23), (43, 43, 43), (43, 19, 1), (50, 125, 25), (26, 117, 13), (27, 18, 9), (78, 117, 39)]
result = {True: 'Passed', False: 'Failed'}
gcdIter_test_results = [result[test_[2] == gcdIter(test_[0], test_[1])] for test_ in tests]
print(gcdIter_test_results)


def gcdRecur(a, b):
    if b == a or b == 0:
        return a
    elif a == 0:
        return b
    return gcdRecur(b, a%b)

gcdRecur_test_results = [result[test_[2] == gcdRecur(test_[0], test_[1])] for test_ in tests]
print(gcdRecur_test_results)


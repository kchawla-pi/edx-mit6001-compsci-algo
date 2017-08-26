def test_isIn():
    chars = ('t', 'g', 'z', 'm', 'w', 'f')
    strings = ('dtshelcoaiwplff', 'sddswaclPOSwdf', 'oglyvondakianusy')
    all_tests = ((True, False, False, False, True, True),
             (False, False, False, False, True, True),
             (False, True, False, False, False, False)
             )
    true_is_pass = {True: 'Passed', False: 'Change'}
    for string_, tests in zip(strings, all_tests):
        print(string_, procStr(string_), chars, [test_ == isIn(char_, procStr(string_)) for char_, test_ in zip(chars, tests)])


def procStr( aStr):
    aStr = aStr.lower()
    aStr = list(aStr)
    aStr.sort()
    aStr = ''.join(aStr)
    return aStr


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[-1] == char:
        return True
    elif len(aStr) % 2 == 0:
        aStr = aStr[:-1]
        
    mid_idx = len(aStr) // 2
    
    if aStr[mid_idx] == char:
        return True
        
    aStr = aStr[mid_idx+1:] if char > aStr[mid_idx] else aStr[:mid_idx+1]
    return isIn(char, aStr)

test_isIn()

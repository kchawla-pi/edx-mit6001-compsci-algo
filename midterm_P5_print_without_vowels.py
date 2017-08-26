"""
Write a Python function that takes in a string and prints out a version of this string that does not
 contain any vowels, according to the specification below.
 Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!.
If s = "a" then print_without_vowels will print the empty string .
"""


def test_print_without_vowels(test_cases):
    msg = "{}. In: {}, Returned: {}, Expected: {}"
    test_results = [msg.format('Passed',
                               test_cases[case_][0],
                               print_without_vowels(test_cases[case_][0], submit=False),
                               test_cases[case_][1])
                    if print_without_vowels(test_cases[case_][0], submit=False) == test_cases[case_][1] else
                    msg.format('Change code' ,
                               test_cases[case_][0],
                               print_without_vowels(test_cases[case_][0], submit=False),
                               test_cases[case_][1])
                    for case_ in test_cases
                    ]
    return test_results
    

def print_without_vowels(s, submit=True):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = ''.join([char_ for char_ in s if char_ not in vowels])
    try:
        result
    except NameError:
        result = None
    if submit:
        print(result)
    else:
        return result


if __name__ == '__main__':
    from pprint import pprint
    test_cases = {1: ("This is great!", "Ths s grt!"),
                    2: ('s', 's'),
                    3: ('S', 'S'),
                    4: ('o', ''),
                    5: ('E', ''),
                    6: ("Earth is the 3rd planet of our solar system. 0k? oKAy!",
                        "rth s th 3rd plnt f r slr systm. 0k? Ky!"),
                    7: ('456', '456'),
                    8: ('#$%', '#$%')
                  }
    pprint(test_print_without_vowels(test_cases))

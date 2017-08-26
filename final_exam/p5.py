def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {from_char: to_char for from_char, to_char in zip(map_from, map_to)}
    decoded = ''.join([key_code[char_] for char_ in code])
    return key_code, decoded
    
def create_test_data():
    test_data = {
        ('basd', 'sdab', 'dbssab'): ({'b': 's', 'a': 'd', 's': 'a', 'd': 'b'}, 'bsaads'),
        ("abcd", "dcba", "dab"): ({'a': 'd', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc'),
        }
    return test_data
    
    
def test_cipher():
    test_data = create_test_data()
    for test_, expected in test_data.items():
        assert cipher(*test_) == expected
    

if __name__ == '__main__':
    test_cipher()

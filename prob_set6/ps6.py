import string


### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name, silent=True):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    if not silent:
        print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    if not silent:
        print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.message_text_encrypted = None
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = dict()
    
    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    
    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        
        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        for stringStream in (string.ascii_lowercase, string.ascii_uppercase):
            dictUnshifted = {idx: letter for idx, letter in enumerate(stringStream)}
            dictShifted = {idx + shift: letter for idx, letter in enumerate(stringStream[:-shift])}
            dictShifted.update({idx: letter for idx, letter in enumerate(stringStream[-shift:])})
            self.encrypting_dict.update(
                        {dictShifted[key]: dictUnshifted[key] for key in dictUnshifted})
        return self.encrypting_dict
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.build_shift_dict(shift)
        message_text_copy = self.message_text
        self.message_text_encrypted = ''.join(
                    [self.encrypting_dict.get(letter, letter) for letter in message_text_copy])
        return self.message_text_encrypted


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
    
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
    
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()
    
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text_decrypted = None
        self.shift = None
        self.decrypting_dict = dict()
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        def words_in_string(text):
            txt_dict = {idx: char_ for idx, char_ in
                        enumerate(text)}  # str[idx] == char -> dict[idx] == char
            txt_dict.update({idx: ' ' for idx, char_ in txt_dict.items() if
                             char_ not in string.ascii_letters + ' '})  # replace non-letters with spaces.
            letters_only = ''.join([txt_dict[idx] for idx in
                                    range(len(txt_dict))])  # dict[idx] == char -> str[idx] == char
            words = letters_only.split()  # words
            return words
        
        def possible_decryptions(encrypted_words):
            """
            Generator to yield decrypted message text
            :param encrypted_words: list of encrypted words which are to be decrypted
            :type encrypted_words: list(str)
            :return: Generator yielding list of possible word decryptions
            :rtype: Generator
            """
            return (
                [Message(word_).apply_shift(26 - shift) for word_ in encrypted_words]
            # decrypt each word using shift value
                for shift in
            range(0, 26))  # try every shift value, 0 incl so list index == shift val.
        
        def estimate_shift(decryptions):
            # yields list of truth values for decrypted word == actual word
            words_validity = (
                [is_word(self.valid_words, word) for word in words_list_ if len(word) > 2]
                # test longer words are actual words
                for words_list_ in decryptions  # wordlist from decrypted text
                )
            
            decryption_scores = [sum(word_validity_) for word_validity_ in
                                 words_validity]  # max real words == plaintext
            best_shift_estimates = [idx for idx, score in enumerate(decryption_scores) if
                                   score == max(decryption_scores)]
            return best_shift_estimates
        
        message_text_copy = self.message_text
        message_words = words_in_string(text=message_text_copy)
        calculated_decryptions = possible_decryptions(encrypted_words=message_words)
        best_shift = estimate_shift(decryptions=calculated_decryptions)
        
        try:
            best_unshift = 26 - best_shift[0] if best_shift[
                0] else 0  # if best_unshift is 26, self.shift == 0
        except TypeError:  # decryption fails if no best shift value
            self.message_text_decrypted = None
            self.shift = None
        else:
            self.message_text_decrypted = self.apply_shift(best_unshift)
            self.shift = best_unshift
        
        finally:
            return self.shift, self.message_text_decrypted


def old_tests():
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    plain_text = " Mary had a little lamb. The lambgets hungry;She can't party till 12!"
    shift = 5
    encrypted_text = Message(plain_text).apply_shift(shift)
    
    plain_encrypted = [
        {
            'plain': " Mary had a little lamb. The lambgets hungry;She can't party till 12!",
            'encrypted': "Rfwd mfi f qnyyqj qfrg. Ymj qfrgljyx mzslwd;Xmj hfs'y ufwyd ynqq 12!",
            'shift': shift,
            },
        ]
    
    ciphertext = CiphertextMessage(encrypted_text).decrypt_message()
    print(ciphertext)
    
    quit()
    
    def outputStack0(obj, test_):
        print(type(test_obj).__name__, spacer, 'type(test_obj)')
        print(test_obj.message_text, spacer, 'test_obj.message_text')
        print(test_obj.valid_words == True, spacer, 'test_obj.valid_words == True')
        print(test_obj.encrypting_dict == True, spacer, 'test_obj.encrypting_dict == True')
        try:
            print(test_obj.shift, spacer, 'test_obj.shift')
            print('\\', test_obj.message_text_encrypted, '/', sep='', end='')
            print(spacer, 'test_obj.message_text_encrypted')
            print('\\', test_[2], '/', sep='', end='')
            print(spacer, 'test_[2]')
            print(test_obj.message_text_encrypted == test_[2],
                  "test_obj.message_text_encrypted == test_[2]")
        except AttributeError:
            pass
    
    def outputStack1(test_obj, test_):
        op_stack = {
            'class': type(test_obj).__name__,
            'message_text': test_obj.message_text,
            'shift': test_obj.shift,
            'message_text_encrypted': test_obj.message_text_encrypted,
            'expected_message_text_encrypted': test_[2],
            'actual_message_text_encrypted == expected_message_text_encrypted': test_obj.message_text_encrypted ==
                                                                                test_[2],
            'valid_words': test_obj.valid_words,
            'encrypting_dict': test_obj.encrypting_dict,
            'shift_dict': test_obj.change_shift(15)
            }
        keys = [
            'class',
            'message_text',
            'shift',
            'message_text_encrypted',
            'expected_message_text_encrypted',
            'actual_message_text_encrypted == expected_message_text_encrypted',
            ]
        for key_ in keys:
            print(key_, '-', op_stack.get(key_, None))
        return op_stack
    
    tests = (
        ('hello', 0, 'hello'),
        ('hello', 2, 'jgnnq'),
        ('we are taking 6.00.1x', 22, 'sa wna pwgejc 6.00.1t'),
        ('th!s is Problem Set 6?', 25, 'sg!r hr Oqnakdl Rds 6?'),
        ('TESTING.... so many words we are testing out your code: last one', 1,
         'UFTUJOH.... tp nboz xpset xf bsf uftujoh pvu zpvs dpef: mbtu pof'),
        ('this is a short message', 0, 'this is a short message'),
        ('this is a short message', 2, None)
        )
    
    # test_obj = Message(tests[0][0])
    from pprint import pprint
    
    test_data_change_shift = (6, 15, 21, 24)
    
    # for new_shift in test_data_change_shift:
    #     for test_ in tests:
    #         print()
    #         orig_shift = test_[1]
    #         test_obj = PlaintextMessage(test_[0], orig_shift)
    #         spacer = ' ' * 5
    #
    #         # outputStack0(obj=test_obj, test_=test_)
    #         # outputStack1(test_obj=test_obj, test_=test_)
    #         init_with_new_shift = PlaintextMessage(test_[0], new_shift)
    #
    #         test_obj.change_shift(new_shift)
    #
    #         # outputStack1(test_obj=test_obj, test_=test_)
    #
    #         message_text = (test_obj.get_message_text(), init_with_new_shift.get_message_text())
    #         print('obj.get_message_text():\t', *message_text, message_text[0] == message_text[1])
    #
    #         message_text_encrypted = (test_obj.get_message_text_encrypted(), init_with_new_shift.get_message_text_encrypted())
    #         print('obj.get_message_text_encrypted():\t', *message_text_encrypted, message_text_encrypted[0] == message_text_encrypted[1])
    #
    #         get_shift = (test_obj.get_shift(), init_with_new_shift.get_shift())
    #         print('obj.get_shift():\t', *get_shift, get_shift[0] == get_shift[1])
    #
    #         input('Enter for next test case: ')
    #
    #     input('Enter for next shift_change: ')
    
    
    # test_obj = []
    # for test_ in tests:
    #     print('..' * 30, test_)
    #     for class_ in classes:
    #         print('\n', '..' * 25, class_.__name__)
    #         try:
    #             msg = class_(*test_)
    #         except TypeError:
    #             msg = class_(test_[0])
    #         print()
    #         print(msg.get_message_text(), ' '*5, ':msg.get_message_text():')
    #         print(msg.build_shift_dict(0))
    #         (msg.build_shift_dict(2))
    #         print(msg.apply_shift(0), ' '*5, ":msg.apply_shift(0):")
    #         print(msg.apply_shift(2), ' '*5, ":msg.apply_shift(2):")
    #         try:
    #             print(msg.get_message_text_encrypted(), ' '*5, ':msg.get_message_text_encrypted():')
    #         except AttributeError:
    #             pass
    #         input()
    #     test_obj.append(msg)
    #     del msg
    #     #     print(msg.change_shift(15))
    #     #     print('.'*75)


def decrypt_story(encrypted_string):
    """
    Decrypts a string encrypted with substitution encryption.
    Returns tuple(shift value, decrypted text)
    
    :param encrypted_string: encrypted string which is to be decrypted.
    :type encrypted_string: str
    :return: (shift value, decrypted text)
    :rtype: tuple(int, str)
    """
    pass
    '''
    Decrypts the encrypted text in 3 blocks of 20 characters and calculates the probable
    shift value. If a common shift value is not found, increases block length by 5 characters in
    each loop and reattempts.
    Once shift value is found, decrypts the remaining string using that shift value.
    '''
    str_length = len(encrypted_string)
    loop = True
    block_length = 20  # initial block length
    while loop:
        blocks = {
            'start': range(0, str_length - block_length, block_length),
            'end': range(block_length, str_length, block_length),
            }
        
        # yields a sliding window for the encrypted string.
        text_blocks = (encrypted_string[start: end] for start, end in
                       zip(blocks['start'], blocks['end']))
        
        # yields the shift value & decrypted version of the block.
        decrypted_blocks = (CiphertextMessage(text_block_).decrypt_message() for text_block_ in
                            text_blocks)
        
        ''' decrypts the first 3 blocks of the encrypted text, returns
         list[tuple(shift value, decrypted block)] '''
        decryption_testing = [next(decrypted_blocks) for i in (0, 1, 2)]
        
        probable_shift = set(
                    test_[0] for test_ in decryption_testing)  # set(shift values from each block
        if len(probable_shift) > 1:  # len(set) > 1 == > multiple possible shift values.
            block_length += 5  # increase block length for improved accuracy, retry
        else:
            loop = False
            resume_from = block_length * 3
            probable_shift = list(probable_shift)[0]
    decrypted_so_far = ''.join([test_[1] for test_ in decryption_testing])
    decrypted_string = decrypted_so_far + Message(encrypted_string[resume_from:]).apply_shift(
        probable_shift)
    return probable_shift, decrypted_string


print("reading encrypted text...")
story_string = get_story_string()
print("Attempting to determine decryption key. Please be patient...")
decrypted_story = decrypt_story(story_string)
print(decrypted_story)


# print(story_string)
# encrypted_story = CiphertextMessage(story_string).decrypt_message()
# print(encrypted_story)

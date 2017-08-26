import string


class Message(object):
    
    def __init__(self, text):
        self.message_text = text
        self.encrypting_dict = dict()
        
    def build_shift_dict(self, shift):
        for stringStream in (string.ascii_lowercase, string.ascii_uppercase):
            dictUnshifted = {idx: letter for idx, letter in enumerate(stringStream)}
            dictShifted = {idx + shift: letter for idx, letter in enumerate(stringStream[:-shift])}
            dictShifted.update({idx: letter for idx, letter in enumerate(stringStream[-shift:])})
            self.encrypting_dict.update({dictShifted[key]: dictUnshifted[key] for key in dictUnshifted})
        return self.encrypting_dict

    def apply_shift(self, shift):
        message_text_copy = self.message_text
        self.message_text = ''.join(
                    [self.encrypting_dict.get(letter, letter) for letter in message_text_copy])
        return self.message_text
    
tests = (
    ('hello', 0, 'hello'),
    ('hello', 2, 'jgnnq'),
    ('we are taking 6.00.1x', 6, 'ck gxk zgqotm 6.00.1d'),
    ('th!s is Problem Set 6?',11, 'es!d td Aczmwpx Dpe 6?'),
    ('TESTING.... so many words we are testing out your code: last one', 24, 'RCQRGLE.... qm kylw umpbq uc ypc rcqrgle msr wmsp ambc: jyqr mlc'),
    )
msg = []
for idx, (text, shift, expected) in enumerate(tests):
    print(idx, text, shift)
    msg.append(Message(text))
    encrypting_dict = msg[idx].build_shift_dict(shift)
    encrypted_msg = msg[idx].apply_shift(shift)

    print(encrypted_msg == expected)

"ck gxk zgqotm 6.00.1d"

msg = Message('this is a short message')
print(msg.get_message_text())
print(msg.build_shift_dict(0))
print(msg.build_shift_dict(2))
print(msg.apply_shift(0))
print(msg.apply_shift(2))

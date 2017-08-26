aTup = ('I', 'am', 'a', 'test', 'tuple')
result = ('I', 'a', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return tuple(elem for idx, elem in enumerate(aTup) if (idx % 2 == 0))

print(oddTuples(aTup) == result)

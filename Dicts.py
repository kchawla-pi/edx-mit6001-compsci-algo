
# num_animals = sum([len(elem) for elem in list(animals.values())])

# print(num_animals)
# print(max(list(map(len, list(animals.values())))))


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    return sum(list(map(len, list(aDict.values()))))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    most_vals = max(list(map(len, list(aDict.values()))))
    return [key for key, val in aDict.items() if len(val) == most_vals][0]


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

biggest(animals)



    

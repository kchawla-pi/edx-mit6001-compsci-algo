from ps4a_mymod import *

#
# Test code
# You don't need to understand how this test code works (but feel free to look it over!)

# To run these tests, simply run this file (open up in your IDE, then run the file as normal)

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, ("fork", 4):94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_getWordScore()")
            print("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_getWordScore()")

# end of test_getWordScore


def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)
        
        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    print("SUCCESS: test_updateHand()")

# end of test_updateHand

def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified wordList?")
            wordInWL = word in wordList
            print("The word", word, "should be in wordList - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "even"

    if  isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)")
        
        failure = True        

    if not failure:
        print("SUCCESS: test_isValidWord()")


def createTestData():
    from collections import namedtuple
    
    NewHandData = namedtuple('NewHandData', 'origHand handSize')
    TestData = namedtuple('TestData', 'currentHand userInput wordScore handScore')
    TestCase = namedtuple('TestCase', 'testCase')
    return {
        0: (
            TestCase(testCase='0'),
            NewHandData(origHand={'h': 1, 'i': 1, 'c': 1, 'z': 1, 'm': 2, 'a': 1}, handSize=7),
            TestData(currentHand='a c i h m m z', userInput='him', wordScore=24, handScore=24),
            TestData(currentHand='a c m z', userInput='cam', wordScore=21, handScore=45),
            TestData(currentHand='z', userInput='.', wordScore=None, handScore=45)
            ),
        1: (
            TestCase(testCase='1'),
            NewHandData(origHand={'w': 1, 's': 1, 't': 2, 'a': 1, 'o': 1, 'f': 1}, handSize=7),
            TestData(currentHand='a c i h m m z', userInput='tow', wordScore=18, handScore=18),
            TestData(currentHand='a s t f', userInput='tasf', wordScore=None, handScore=18),
            TestData(currentHand='a s t f', userInput='fast', wordScore=28, handScore=46),
            TestData(currentHand='', userInput=None, wordScore=None, handScore=46)
            ),
        2: (
            TestCase(testCase='2'),
            NewHandData(origHand={'n': 1, 'e': 1, 't': 1, 'a': 1, 'r': 1, 'i': 2}, handSize=7),
            TestData(currentHand='a r e t i i n', userInput='inertia', wordScore=99, handScore=99)
            ),
        't3': (
            TestCase(testCase='Test 3: Guessing word, then quitting'),
            NewHandData(origHand={'i': 1, 'o': 1, 'q': 1}, handSize=3),
            TestData(currentHand='i o q', userInput='qi', wordScore=22, handScore=22),
            TestData(currentHand='o', userInput='.', wordScore=None, handScore=22)
            ),
        't4': (
            TestCase(testCase="Test 4: Can't make a word"),
            NewHandData(origHand={'b': 1, 's': 1, 'x': 2, 'y': 1, 'z': 2}, handSize=7),
            TestData(currentHand='x x s y b z z', userInput='.', wordScore=None, handScore=0)
            ),
        't6': (
            TestCase(testCase="Test 6: Full hand transcript - can't use every letter"),
            NewHandData(origHand={'a': 2, 'e': 1, 'p': 2, 'r': 1, 'z': 1}, handSize=7),
            TestData(currentHand='z a a r p p e', userInput='pear', wordScore=24, handScore=24),
            TestData(currentHand='a p z', userInput='za', wordScore=22, handScore=46),
            TestData(currentHand='p', userInput='p', wordScore=None, handScore=46),
            TestData(currentHand=None, userInput='p', wordScore=None, handScore=46)
            ),
        't7': (
            TestCase(testCase="Test 7: Randomized Test"),
            NewHandData(origHand={'a': 2, 'c': 1, 'e': 1, 'h': 1, 'm': 3, 'r': 1, 's': 1},
                        handSize=10),
            TestData(currentHand='a a e r h m m m c s', userInput='m', wordScore=None,
                     handScore=None),
            TestData(currentHand='a a e r h m m m c s', userInput='chayote', wordScore=None,
                     handScore=None),
            TestData(currentHand='a a e r h m m m c s', userInput='kwijibo', wordScore=None,
                     handScore=None),
            TestData(currentHand='a a e r h m m m c s', userInput='hammer', wordScore=78,
                     handScore=78),
            TestData(currentHand='a m c s', userInput='.', wordScore=None, handScore=78)
            ),
        't1': (
            TestCase(testCase='Test 1: Using all the letters in the hand on the first guess'),
            NewHandData(origHand={'a': 1, 'h': 1, 'i': 1, 'r': 1}, handSize=4),
            TestData(currentHand='i a h r', userInput='hair', wordScore=78, handScore=78),
            TestData(currentHand='', userInput=None, wordScore=None, handScore=None)
            ),
        't2': (
            TestCase(testCase="Test 2: Guessing incorrectly, then correctly"),
            NewHandData(origHand={'a': 1, 'z': 1}, handSize=2),
            TestData(currentHand='a z', userInput='zo', wordScore=None, handScore=None),
            TestData(currentHand='', userInput='za', wordScore=72, handScore=72)
            ),
        't5': (
            TestCase(testCase="Test 5: Full hand transcript - using all letters"),
            NewHandData(origHand={'a': 2, 'e': 2, 'p': 1, 'r': 1, 't': 1}, handSize=7),
            TestData(currentHand='t a a r p e e', userInput='pear', wordScore=24, handScore=24),
            TestData(currentHand='a t e', userInput='tea', wordScore=9, handScore=33)
            )
        }


def test_playHand(wordList):
    def test4(testData, testKey, wordList):
        test_= testData[testKey]
        hand = test_[1].origHand
        handSize = test_[1].handSize
        playHand(hand=hand, wordList=wordList, handSize=handSize)

    testData = createTestData()
    testSuite = ['t3', 't4', 't6', 't7', 't5', 't2', 't1']
    testSuite.sort()
    for testKey in testSuite:
        print('_' * 50)
        # print(testKey)
        test4(testData=testData, testKey=testKey, wordList=wordList)

if __name__ == '__main__':
    
    wordList = loadWords()
    print("----------------------------------------------------------------------")
    print("Testing getWordScore...")
    test_getWordScore()
    print("----------------------------------------------------------------------")
    print("Testing updateHand...")
    test_updateHand()
    print("----------------------------------------------------------------------")
    print("Testing isValidWord...")
    test_isValidWord(wordList)
    print("----------------------------------------------------------------------")
    # test_playHand(wordList)
    print("----------------------------------------------------------------------")
    print("All done!")

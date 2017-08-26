# The 6.00 Word Game

import random
import string
import timeit

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
    }

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # # inFile: file
    # inFile = open(WORDLIST_FILENAME, 'r')
    # # wordList: list of strings
    # wordList = []
    # for line in inFile:
    #     wordList.append(line.strip().lower())
    # print("  ", len(wordList), "words loaded.")
    # return wordList

    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME, 'r') as readObj:
        lines = readObj.readlines()
    # wordList: list of strings
    wordList = []
    for line in lines:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary (letter (str) -> count (int))
    """
    # freqs: dictionary (element_type -> int)
    return {letter: sequence.count(letter) for letter in sequence}
    

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, handSize):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all handSize
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    handSize: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    scores = [SCRABBLE_LETTER_VALUES[letter] for letter in word]
    scrabble_bonus = 50 if len(word) == handSize else 0
    return sum(scores) * len(word) + scrabble_bonus


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand, sorted alphabetically.
    
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
       a e l l l x x
    
    hand: dictionary (string -> int)
    return: None
    """
    tempList = [letter * freq for letter, freq in hand.items()]
    tempList.sort()
    tempList = list(''.join(tempList))
    print(' '.join(tempList),'\n')

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(handSize):
    """
    Returns a random hand containing handSize lowercase letters.
    At least handSize/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    handSize: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = handSize // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(numVowels, handSize):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    
    return hand


#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    wordFreq = getFrequencyDict(word)
    handCopy = hand.copy()
    handCopy.update({letter: handCopy[letter] - wordFreq[letter] for letter in wordFreq})
    return handCopy


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    wordFreq = getFrequencyDict(sequence=word)
    lettersFromHand = [
        int(wordFreq[letter] <= hand.get(letter, 0)) for letter in wordFreq
        ]  # 1 if letter count in (word <= hand) else 0
    fromHand = sum(lettersFromHand) == len(lettersFromHand)  # if sum of 1s == len of list then all letters legal
    return fromHand and word in wordList


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


def validPlay(word, hand, handScore, handSize):
    wordScore = getWordScore(word=word, handSize=handSize)
    handScore += wordScore
    hand = updateHand(hand=hand, word=word)  # Update the hand
    return wordScore, handScore, hand
    

def playHand(hand, wordList, handSize):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      handSize: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    origHand = hand
    handScore = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand):
        
        # Display the hand
        print("Current hand:", end=' ')
        displayHand(hand)
        # Ask user for input
        choice = input('Enter word, or a "." to indicate that you are finished: ')
        
        if choice == '.':  # If the input is a single period:
            endMsg = "Goodbye!"
            break  # End the game (break out of the loop)
        else:  # Otherwise (the input is not a single period):
            word = choice
        
        wordValid = isValidWord(word=word, hand=hand, wordList=wordList)
        if not wordValid:  # If the word is not valid:
            print("Invalid word, please try again.\n")  # Reject invalid word (print a message followed by a blank line)
        else:  # Otherwise (the word is valid):
            wordScore, handScore, hand = validPlay(word=word, hand=hand, handScore=handScore, handSize=handSize)
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print('" {} " earned {} points. Total: {} points\n'.format(word, wordScore, handScore))
            endMsg = "Run out of letters."
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("{} Total score: {} points.".format(endMsg, handScore))


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    def userIntentQuery():
        choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").lower()
        if choice == 'e':
            return
        elif choice == 'r':
            try:
                return hand
            except NameError:
                print("You have not played a hand yet. Please play a new hand first!\n")
                return userIntentQuery()
        elif choice == 'n':
            return dealHand(handSize=HAND_SIZE)
        else:
            print("Invalid command.")
            return userIntentQuery()
    
    while True:
        hand = userIntentQuery()
        if hand:
            playHand(hand=hand, wordList=wordList, handSize=HAND_SIZE)
            print()
        else:
            break
        


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    print(wordList)
    # playGame(wordList)
    # hands = (
    #     ({'a': 1, 'e': 1, 'h': 1, 'm': 2, 'r': 1}, 6),
    #     ({'a': 1, 'z': 1}, 2),
    #     ({'i': 1, 'o': 1, 'q': 1}, 3),
    #     ({'b': 1, 's': 1, 'x': 2, 'y': 1, 'z': 2}, 7),
    #     ({'a': 2, 'e': 2, 'p': 1, 'r': 1, 't': 1}, 7),
    #     ({'a': 2, 'e': 1, 'p': 2, 'r': 1, 'z': 1}, 7),
    #     ({'b': 1, 'c': 1, 'd': 1, 'k': 1, 'm': 1, 'r': 1, 's': 1, 'u': 1, 'y': 1, 'z': 1}, 10)
    #     )
    # for hand_ in hands:
    #     print(playHand(hand=hand_[0], wordList=wordList, n=2))
    #     print('_' * 50)

# newHand = dealHand(n=HAND_SIZE)
hands = (
    {'h': 1, 'i': 1, 'c': 1, 'z': 1, 'm': 2, 'a': 1},
    {'w': 1, 's': 1, 't': 2, 'a': 1, 'o': 1, 'f': 1},
    {'n': 1, 'e': 1, 't': 1, 'a': 1, 'r': 1, 'i': 2},
    {'h': 1, 'i': 1, 'c': 1, 'm': 2, 'a': 1},
    {'s': 1, 't': 2, 'a': 1, 'o': 1, 'f': 1},
    {'n': 1, 'e': 1, 't': 1, 'a': 1, 'r': 1, 'i': 2, 'l': 1},
    {'i': 1, 'o': 1, 'q': 1},
    {'b': 1, 's': 1, 'x': 2, 'y': 1, 'z': 2},
    {'a': 2, 'e': 1, 'p': 2, 'r': 1, 'z': 1},
    {'a': 2, 'c': 1, 'e': 1, 'h': 1, 'm': 3, 'r': 1, 's': 1}
    )


def test1(hands):
    hands = (hands[2], hands[5])
    for hand_ in hands:
        pass
        print()
        handSize = sum(hand_.values())
        # print(hand_, handSize, sum(hand_.values()))
        playHand(hand=hand_, wordList=wordList, n=handSize)


def test2(hands):
    for hand_ in hands:
        pass
        print()
        handSize = sum(hand_.values())
        print(hand_, handSize, sum(hand_.values()))
        playHand(hand=hand_, wordList=wordList, n=handSize)


def test3(testData):
    for testName, testInfo in testData.items():
        hand = testInfo[0].origHand
        # handSize_calc = sum(hand.values())
        handSize = testInfo[0].handSize
        # print(hand, handSize)
        playHand(hand=hand, wordList=wordList, n=handSize)
        # break

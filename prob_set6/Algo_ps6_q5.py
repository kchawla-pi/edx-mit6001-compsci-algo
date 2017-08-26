import itertools
import random



def search(L, e):
    print("search:", L, e)
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    print("newsearch:", L, e)
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


def swapSort(L):
    """ L is a list on integers """
    # print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                # print(L)
    # print("Final L: ", L)

def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


# L = sorted([random.randint(0,1000) for i in range(0, 1)])
# eList = sorted([random.randint(0,1000) for i in range(0, 10)])
#
# search_result = [search(L, e) for e in eList]
# newsearch_result = [newsearch(L, e) for e in eList]
#
#
#
# print(search_result)
# # print(search(L, L))
# print()
# print(newsearch_result)
# # print(newsearch(L, L))
import time
from pprint import pprint

start= []
end = []
sizes = []

start2 = []
end2 = []
sizes2 = []

limit = 20
for size_ in range(1, limit, 10):
    L = [random.randint(0,1000) for i in range(0, size_)]
    sizes.append(size_)
    start.append(time.time())
    swapSort(L)
    end.append(time.time())
    
    diff = [(size_, round(end_ - start_, 2)) for size_, start_, end_ in zip(sizes, start, end)]
    print(L)
    pprint(diff[-1])

    sizes2.append(size_)
    start2.append(time.time())
    swapSort(L)
    end2.append(time.time())
    
    diff2 = [(size_, round(end_ - start_, 2)) for size_, start_, end_ in zip(sizes2, start2, end2)]
    print(L)
    pprint(diff[-1])





# swapSort(L)

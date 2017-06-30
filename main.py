import os
import sys
import collections
import heapq
from heapq import heappop
from heapq import heappush
from random import random
from functools import total_ordering

# binary tree
@total_ordering
class Node(object):
    """
        Binary Tree
    """
    def __init__(self, key=None, weight=None):
        # key
        self._key = key
        # weight
        self._weight = weight
        # to break tie uniformaly randomly
        self._random = random()
        # two child, binary tree
        self._children = []

    def addChild(self, obj):
        """
        add Child
        """
        self._children.append(obj)

    def __eq__(self, other):
        return (self._weight, self._random) == (other._weight, other._random)

    def __lt__(self, other):
        return (self._weight, self._random) < (other._weight, other._random)


def strToFreq(T):
    """
    String To Frequency
    """
    return [(k, v) for k, v in dict(collections.Counter(T)).items()]

def huffmanEncode(Freq):
    # initialize priority queue
    data = [Node(x[0], x[1]) for x in Freq]
    # for a min heap
    heapq.heapify(data)

    while len(data) >= 2:
        child1 = heappop(data)
        child2 = heappop(data) 
        parent = Node(None, child1._weight + child2._weight)
        parent.addChild(child1)
        parent.addChild(child2)

        heappush(data, parent)

    return data

def traverseTree(root, Code, keyCode):
    if len(root._children) == 0:
        keyCode[root._key] = Code
        return
    # left child
    traverseTree(root._children[0], Code+'0', keyCode)
    #right child
    traverseTree(root._children[1], Code+'1', keyCode)


def encodeStr(inputStr, root):
    Code = ""
    keyCode = dict()
    traverseTree(root[0], Code, keyCode)
    print(keyCode)
    
    result = ""
    for c in inputStr:
        if c not in keyCode.keys():
            print("character {} not in original string.".format(c))
        result += keyCode[c]

    print(result)
    return result

if __name__ == "__main__":
    x = "abca"
    encodeStr(x, huffmanEncode(strToFreq(x)))

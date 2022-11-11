#####################################################################
# Date: 11/10/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy
#####################################################################
# problem1: Remove Duplicates From LinkedList
# reading question:1m
# notes: sorted 
# thoughts:
# loop through the entire linked list
# at each iteration, remove those successive nodes that have the same value as the current node
# for each node, change its next pointer to the next node that has a different value

# coding and testing: 20m
# O(n) time | O(1) space

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList # linkedList is initialized to be the head, the first node in the linkedList
    while currentNode is not None: # meaning currentNode.next is not none, nodes#>1
        nextDistinctNode = currentNode.next 
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next 
        currentNode.next = nextDistinctNode # if currentNode.next = None, which means it reaches at the end of the linkedlist, the currentNode is the last node
        currentNode = nextDistinctNode # find different value, move currentNode and nextDistinctNode onto the same node?
    return linkedList


############################################################################
# problem2: First Non-Repeating Character
# reading question: 1m
# notes:only lowercase alphabet characters
# data structure choice: hash table
# countFrequencies[char] = countFrequencies.get(char, 0)+1

# thoughts:
# traverse the entire string once to fill the hash table
# do a second traversal to find the first character with a frequency of 1 by using the hash table's constant-time lookups

# O(n) time | O(1) space, since input only contains lowercase letter, the length of the hash table will be up to 26




########################################################################
# problem3: Node Depths
# reading question: 3m
# notes: recursion
# thoughts: 
# start at root node whose depth is 0, pass the depth down by increasing 1 at each level to the children nodes and sum up all depths recursively
# depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

# O(n) time | O(h) space, where h is the height of the tree


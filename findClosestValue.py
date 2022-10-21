# *********to keep track of time on reading question, coding and testing*********
# reading question: 1
# coding: 21
# test code successfully: 4

# thoughts: recursive approach
# traverse the BST node by node while keep track of node with value closest to the target value
# compute the absolute value of the difference between a node's value and the target's value
# update the current closest value if any node is closer to the target than the current one

# Average case: O(logn) time | O(logn) space
# Worst case: O(n) time | O(n) space 
def findClosestValueInBst(tree, target):
    # return helper(tree, target, float("inf"))
    return helper(tree, target, tree.value) #initialize closest value to be the first value of the root node

def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if target > tree.value:
        return helper(tree.right, target, closest)
    elif target < tree.value:
        return helper(tree.left, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
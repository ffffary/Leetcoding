# track time of reading question, coding, testing
# reading question: 1 min
# coding: 10 min
# test code successfully: 2 min

# thoughts:
# start from the root, go all the way down the branch before exploring the next branch 
# O(V + E) time | O(V) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name 
    # add a child to the node by appending a new node to the children array
    def addChild(self, name):
        self.children.append(Node(name))
    # for every child in the children array, call DFS on the child, then pass them to the final array
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

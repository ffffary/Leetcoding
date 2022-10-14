# track time of reading question, coding, testing
# reading question: 
# coding: 
# test code successfully:

# thoughts: 

# O(logn) time | O(1) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n-2) + getNthFib(n-1)

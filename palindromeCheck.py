# *********to keep track of time on reading question, coding and testing*********
# reading question: 1m
# coding: 12m
# test code successfully:2m

# thoughts: iterative (two pointers) approach
# start with 2 pointers, one pointing at the leftmost and the other pointing at the rightmost
# compare the two, if they are equal to each other, keep moving, otherwise, return False
# repeat until the 2 pointers overlap, then we are done

# O(n) time | O(1) space

# def isPalindrome(string):
#     left = 0
#     right = len(string)-1
#     if len(string) == 1: 
#         return True
#     elif len(string) > 1:
#         while left <= right:
#             if string[left] != string[right]:
#                 return False
#             else: 
#                 left += 1
#                 right -= 1
#         return True
#     else:
#         return False

#refined:=>
def isPalindrome(string):
    left = 0
    right = len(string)-1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


#adopt recursive approach: O(n) time | O(n) space because of the call stack
def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[i]:
        return False
    return isPalindrome(string, i+1)

























#intuitive/naive approach:
#create an empty string(O(n^2)) or array/list by using append and join functions with better time complexity O(n)
#reverse the given string and compare the new string with the given string
#if they are equal then return True, otherwise return False
# O(n^2) time | O(n) space
def isPalindrome(string):
    ReversedString = ""
    for i in reversed(range(len(string))):
        ReversedString += string[i] #n*n
    return string == ReversedString

#print(list(reversed(range(10))))
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# O(n) time | O(n) space
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


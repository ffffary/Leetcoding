# *********to keep track of time on reading question, coding and testing*********
# reading question: 2m
# coding: 28m
# test code successfully: 7m

# thoughts: use recursion
# initialize a parameter multiplier standing for the depth, and a sum variable to be 0 
# iterate through the array, check the type of each element
# if it's a list, recursively call the function adding multiplier by 1 and add all elements up; otherwise, just add all up

# O(N) time | O(D) space
# N is the total numbers of elements in the array, including elements in all subarrays
# D is the depth of the innermost array

def productSum(array, multiplier):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element 
    return sum * multiplier





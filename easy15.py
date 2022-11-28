#####################################################################
# Date: 11/27/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy
#####################################################################
# problem1: smallestDifference
# reading question:4m
# coding: 14m
# testing: 1m

# notes:
# only 1 pair of numbers with smallest difference
# a > b: b+=1
# a < b: a+=1

# thoughts:
# sort two arrays and iterate through them once, place a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer values
# if the difference is equal to zero, find the smallest value and return, otherwise, increment the pointer with smaller value to find a potentially better pair with smallest difference value 
# repeat until one of the pointers goes out of index range

# O(nlogn) + O(mlogm) time | O(1) space, where n is the length of arrayOne, m is the length of arrayTwo
def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()

    smallestDiff = float("inf")
    currentDiff = float("inf")

    idxOne = 0
    idxTwo = 0
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum == secondNum:
            return [firstNum, secondNum]
        elif firstNum > secondNum:
            currentDiff = firstNum - secondNum  
            idxTwo += 1
        else:
            currentDiff = secondNum - firstNum   
            idxOne += 1

        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            smallestPair = [firstNum, secondNum]

    return smallestPair

#####################################################################
# problem2: Move Element To End
# reading question: 1m

# notes:
# in-place
# can change order of other integers

#option1-sorting-O(nlogn)
#option2-hash table-has to allocate O(n) space
#option3-achieve linear time without sorting the array

# thoughts:
# place 2 pointers at the first and last of the input array and progressively moving them inwards
# if last pointer value is equal to the toMove, increment the last pointer
# if first pointer value is equal to the toMove but last pointer value unequal to the toMove, swap first with last and increment first pointer
# repeat the process until the two pointers pass each other

# O(n) time | O(1) space


#####################################################################
# problem3: Monotonic Array
# link: https://leetcode.com/problems/monotonic-array/
# reading question: 1m
# coding: 19m
# testing: 3m

# notes: non-increasing(duplicates allowed) or non-decreasing(can have two numbers equal to each other)
# edge case(also counted as monotonic array)-empty array; arrray with one or two elements; duplicates
# thoughts:
# iterate through the input array from left to right, get the direction by making comparisons between 2 elements
# if any comparison breaks the previously identified direction(trending upwards or downwards), return false

# easier method: set boolean constant
# assume the input array is non-decreasing or non-increasing
# iterate through the entire array and check if one or both of the assumptions can be validated.

# O(n) time | O(1) space
def isMonotonic(array):
    isTrendingUpwards = True 
    isTrendingDownwards = True
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isTrendingUpwards = False 
        if array[i] > array[i-1]:
            isTrendingDownwards = False 
    return isTrendingUpwards or isTrendingDownwards


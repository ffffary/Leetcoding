#####################################################################
# Date: 11/18/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy
#####################################################################
# problem1: Insertion Sort
# reading question: 30s
# thoughts:
# divide the input array into 2 subarrays in place, the 1st subarray should be sorted starting with a length of 1, the 2nd subarray should be unsorted
# iterate through the unsorted subarray, insert all the sorted elements into the sorted subarray in the correct position by swapping them into place

# worst & average: O(n^2) time | O(1) space
# best: O(n) time | O(1) space if the given array is almost sorted

#####################################################################
# problem2: Bubble Sort
# reading question: 30s
# notes: to optimize the runtime, after each iteration, we can avoid comparing the last element since it's already in the correct position 
# by adding a counter variable and substract it in the for range loop
# thoughts:
# traverse the input array, starting from the 1st element, compare with its adjacent element, if they are out of order, swap them
# repeat the process until then entire array is sorted

# worst & average: O(n^2) time | O(1) space
# best: O(n) time | O(1) space if the given array is almost sorted

#####################################################################
# problem3: Three Sum
# link: https://leetcode.com/problems/3sum/
# reading question: 1m
# coding: 8m
# testing: 2m

# notes: 
# numbers in each triplet has to be in sorted order
# the triplets should be in sorted order

# option1-brute force using 3 for loops->O(n^3)
# option2-use hash table with 2 for loops->O(n^2)
# option3-two pointers->O(n^2)

# thoughts: 
# sort the array in ascending order and iterate through the array
# for each iteration, place a left pointer immediately to the right of the current number and a right pointer on the final position of the array
# check if the sum of currentnumber, left number, right number is equal to the targetsum

# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    threeSum = []
    # for i in range(len(array)): this line can be optimized since we need 3 numbers add up to the targetsum
    for i in range(len(array)-2): #no need to iterate through the last two 
        left = i + 1
        right = len(array) - 1
        while left < right: #cannot be equal since numbers are distinct
            currentSum = array[i] + array[left] + array[right] 
            if currentSum == targetSum:
                threeSum.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
        
    return threeSum


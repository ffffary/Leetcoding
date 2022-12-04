#####################################################################
# Date: 12/4/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy-medium
#####################################################################
# problem1: Spiral Traverse
# reading question:2m
# notes:
# declare 4 corners of the grid: startRow, endRow, startCol, endCol

# data structure choice: array

# thoughts:
# initialize 4 variables(startRow, endRow, startCol, endCol) to represent the bounds of the first rectangle perimeter in the spiral
# traverse the perimeter using those bounds, then move them inwards
# stop when the starting row passes the ending row or the starting column passes the ending column

# O(n) time | O(n) space

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    
    while startRow <= endRow and startCol <= endCol:
        
        for col in range(startCol, endCol+1):
            result.append(array[startRow][col])
            
        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])
            
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:#deal with edge case(最内层只有一行)
                break
            result.append(array[endRow][col])
            
        for row in reversed(range(startRow+1, endRow)):
            if startCol == endCol:#deal with edge case(最内层只有一列)
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result

#####################################################################
# problem2: Longest Peak 
# reading question: 5m
# notes:
# a valid peak with left edge and right edge must be at least a length of 3: e.g.340
# strictly decreasing/increasing => no duplicates allowed
# first increasing in sequence, reach a tip, goes down in decreasing order
# can have few solutions, but return the solution with the longest length
# peak cannot be at the beginning or end

# thoughts: break big problem into small pieces
# find peak
# find potential expanded left edge and right edge of the peak
# find length of the peak by comparing 

# O(n) time | O(1) space
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array)-1: # peak cannot be at the beginning or end
        # find peaks
        isPeak = array[i] > array[i-1] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue 

        # find potential expanded left edge and right edge of the peak
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1

        # find length of the peak
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(currentPeakLength, longestPeakLength)
        i = rightIdx

    return longestPeakLength

#####################################################################
# problem3: Array of Products
# reading question: 3m
# notes: 
# non-empty array of integers(+ / -)
# solve it without using division

# thoughts: the optimized method-create one additional array
# calculate the product of every element to the left and the product of every elements to the right
# use two for loops iterating through the input array: one from left to right, the other from right to left


# naive approach: two for loops
# O(n^2) time | O(n) space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j:
                product *= array[j]
        products[i] = product 
    return products


# optimized: tons of repeated work-->store the multiplication
# find left side product and right side product, multiply both sides
# [5, 1, 4, 2] ==> if i = 2, then left side is 5x1=5, right side is 2, then the product is 5x2=10
# left: [1, 5, 5, 20] right:[8, 8, 2, 1]
# 确定一个index，算左边的乘积，再算右边的乘积，分别记入left, right array
# then multiply one by one, then get [8, 40, 10, 20]

# why optimized?
# calculate left side product once and store them in an array
# calculate right...and store..., then multiply by same index

# O(n) time | O(n) space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    left = [1 for _ in range(len(array))]
    right = [1 for _ in range(len(array))]

    leftProduct = 1
    for i in range(len(array)):
        left[i] = leftProduct 
        leftProduct *= array[i]

    rightProduct = 1
    for i in reversed(range(len(array))):
        right[i] = rightProduct
        rightProduct *= array[i]

    for i in range(len(array)):
        products[i] = left[i] * right[i]

    return products
    

# can we optimize the space even more? yes, we can just create 1 additional array
# O(n) time | O(1) space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    leftProduct = 1
    for i in range(len(array)):
        products[i] = leftProduct
        leftProduct *= array[i]

    rightProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightProduct
        rightProduct *= array[i]
    
    return products

# track time of reading question, coding, testing
# reading question: 1m
# coding: 15m
# test code successfully: 2m

# thoughts: 
# store all values in a set
# loop through each number in the array, looking for its pairs in the set
# if there is any pair, return the 2 numbers; otherwise loop exits and return empty array

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    container = set(num for num in array)
    for num in array:
        target = targetSum - num
        if target in container and target is not num:
            return [target, num]
    return []


# optimized space time: O(n) -> O(1), time is O(nlogn)
# thoughts:
# sort the array
# use two pointers pointing at the beginning and end of the array respectively
# if the sum is larger than the targetSum, move the right pointer to the left
# otherwise, move the left pointer to the right
#coding: 13m  testing: 1m
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        sum = array[left] + array[right]
        if sum == targetSum:
            return [array[left], array[right]]
        elif sum > targetSum:
            right -= 1
        else:
            left += 1
    return []






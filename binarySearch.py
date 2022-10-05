# track time of reading question, coding, testing
# reading question: 30s
# coding: 11m
# test code successfully:1m

# thoughts: iterative Binary Search
# Compare target with the middle element.
# If it matches with the middle element, return the mid index.
# Else if it's greater, ignore left half
# Else if it's smaller, ignore right half

# # O(logn) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


#recursive Binary Search
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)

# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if array[mid] == target:
#         return mid 
#     elif array[mid] > target:
#         return binarySearchHelper(array, target, left, mid - 1)
#     else:
#         return binarySearchHelper(array, target, mid + 1, right)





# *********to keep track of time on reading question, coding and testing*********
# reading question: 1m
# coding: 14m
# test code successfully:2m

# initial thoughts: brute force takes O(nlogn) time, O(n) space
# simply iterate through the array value by value, square each and insert the squares into the output array, 
# sort the array(to avoid possible negative integers after squaring from messing up the order)

#better idea:
# since the given array is sorted, we can essentially achieve linear time by using two pointers
# to avoid sorting the output array, compare the absolute value of the first element and last element
# if it's bigger, increment the smallerindex by 1, otherwise, decrement the biggerindex by 1


# optimized time complexity: O(n) time | O(n) space
def sortedSquaredArray(array):
    # sortedSquares = [0] * len(array)
    sortedSquares = [0 for _ in array]
    smallestValueIdx = 0
    biggestValueIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        if abs(array[smallestValueIdx]) > abs(array[biggestValueIdx]):
            sortedSquares[idx] = array[smallestValueIdx] * array[smallestValueIdx]
            smallestValueIdx += 1
        else:
            sortedSquares[idx] = array[biggestValueIdx] * array[biggestValueIdx]
            biggestValueIdx -= 1
    return sortedSquares
            
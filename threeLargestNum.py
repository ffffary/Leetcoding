# thoughts:
# initialize an empty array of length three
# iterate through the given array and check if we get the 3rd/2nd/1st largest number of the created array
# compare with the next numbers as we go and update the three largest numbers as needed

# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):# shift and update the 3 largest numbers
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx: # if the pointer is at the last index
            array[i] = num 
        else:
            array[i] = array[i + 1]

# for example: idx = 2
# [0, 1, 2]
# [x, y, z]
# for i in range(0, 2 + 1)
# if i == 2: 
# [0, 1, 2]
# [y, z, num]













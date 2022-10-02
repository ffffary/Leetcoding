#thoughts:
# iterate through the unsorted list, 
# find the smallest number and append it to the sorted sublist, 
# keep doing that until we only have a sorted sublist. 
#O(n^2)time | O(1) space
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array):
        minIdx = currentIdx #the 1st element itself, has nothing to compare
        for i in range(currentIdx + 1, len(array)):
            if array[minIdx] > array[i]: #make compararison starting from the second element
                minIdx = i 
        swap(currentIdx, minIdx, array)
        currentIdx += 1

    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

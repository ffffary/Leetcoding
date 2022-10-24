# *********to keep track of time on reading question, coding and testing*********
# reading question: 1m
# coding: 18m
# test code successfully:1m

# thoughts: 
# initialize 2 pointers, one for the potential subsequence, the other for the main array
# keep moving forward the pointer of the main array, only move the pointer of the subsequence when we find a match
# keep iterating until we reach the end of the subsequence 

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seqIdx = 0
    arrIdx = 0
    while seqIdx < len(sequence) and arrIdx < len(array): 
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


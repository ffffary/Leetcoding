#####################################################################
# Date: 11/7/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy
# Problems source: https://github.com/ffffary/Leetcode-problems-images
#####################################################################
# problem1: Run-Length Encoding

# reading question:3m

# notes:
# lossless: output can get back to input, vice versa
# all kinds of string types(";;;;''222sssBBB----)]***  ")
# given non-empty string: len(string) >= 1
# for x in string: iterate items/elements 
# for x in range: iterate index/numbers

# thoughts:
# traverse the input string and count the length of each run
# if we reach a run of length 9 or the end of a run, append the count and corresponding character
# reset the count to 1 before continuing to traverse the string

# O(n) time | O(n) space
def runLengthEncoding(string):

    encodedStringCharacters = []
    currentRunlength = 1
        
    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i-1]
        if currentCharacter != previousCharacter or currentRunlength == 9:
            encodedStringCharacters.append(str(currentRunlength))
            encodedStringCharacters.append(previousCharacter)
            currentRunlength = 0
        currentRunlength += 1
    #handle edge cases: the very last run, and when string length is only 1
    #set len(string)-1, to make sure we will not run into an index error
    encodedStringCharacters.append(str(currentRunlength))
    encodedStringCharacters.append(string[len(string)-1])
        
    return "".join(encodedStringCharacters)

  
#############################################################################
# problem2: Generate Document
# reading question: 3m
# notes:
# find minimum sum of change that you cannot create
# v > c + 1 => c+1
# v <= c + 1 => v+c

# thoughts:
# sort the array in place and initialize a variable to store the current sum of change that we can create up to
# loop through the array, at each iteration, compare the current coin to the currenChangeSum:
# if the coin value is greater than currenChangeSum+1, return currenChangeSum+1
# otherwise, add the current coin to the currenChangeSum, keep iterating until for loop ends and return currenChangeSum+1

# O(nlogn) time | O(1) space, if sorted in-place, otherwise, O(n)

#############################################################################
# problem3: non-Constructible Change
# reading question: 2m

# notes: 
# duplicated characters allowed in characters
# length of document cannot exceed length of characters
# two arrays given, hash map data structure!

# thoughts: 
# count all characters in characters string and store them in a hash table
# loop through the document string to check if each char in the table has a value greater than zero
# if value doesn't exist or not greater than 0, return False
# otherwise, decrement the char's value until the end of document string, return True


# O(n + m) time | O(c) space if additional space are allowed to allocate
# n, length of characters, m, length of document, c, number of unique characters in characters 

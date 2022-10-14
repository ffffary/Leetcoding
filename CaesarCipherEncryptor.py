# *********to keep track of time on reading question, coding and testing*********
# reading question: 3m
# coding: 34m
# test code successfully:5m

# thoughts: 
# create an array to hold all new chars
# iterate through the input string, append each new letter to the created array 
# by calling the getNewChar function which shifts each char by the given key

# O(n) time | O(n) space

def caesarCipherEncryptor(string, key):
    newString = []
    newKey = key % 26 # to limit larger key value causing multiple wrappings around the alphabet
    for char in string:
        newString.append(getNewChar(char, newKey))
    return "".join(newString)

def getNewChar(char, key):
    newCharCode = ord(char) + key
    if newCharCode <= 122:
        return chr(newCharCode)
    else:
        return chr(96 + newCharCode % 122)


# Convert ASCII Unicode Character 'A' to 65: ord("A") =>65
# y = ord('A')

# Convert integer 65 to ASCII Character ('A'): chr(65) =>A

# ord("a") =>97
# chr(122) =>z


# updated easier coding version with same time&space complexity 
# without ASCII code values conversion
def caesarCipherEncryptor(string, key):
    newString = []
    newKey = key % 26
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    for char in string:
        newString.append(getNewChar(char, newKey, alphabetList))
    return "".join(newString)

def getNewChar(char, key, alphabetList):
    newCharCode = alphabetList.index(char) + key
    return alphabetList[newCharCode % 26]
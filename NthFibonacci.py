# track time of reading question, coding, testing
# reading question: 1m
# coding: 5m
# test code successfully:0.5m

# thoughts: 
# use recursion with memoization would take O(n) time | O(n) space
# iteration method would be preferable for space improvement as the space complexity would be just O(1)
# BUT when n gets humongous, the iteration approach is slower than recursion with memoization


# O(2^n) time | O(n) space   naive approach--->too slow...
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return getNthFib(n-2) + getNthFib(n-1)

# for i in range(1, 51):
#     print(i, ":", getNthFib(i))



# lru_cache: least recently used cache

# easier approach to optimize: memoization
# from functools module import lru_cache decorator
# O(n) time | O(n) space
from functools import lru_cache
@lru_cache(maxsize = 1000)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return getNthFib(n-2) + getNthFib(n-1)



# if we don't use the lru_cache decorator to do memoization, create a hash table/dictionary to store values instead
def getNthFib(n, cache={1: 0, 2: 1}):
    # check if the value has been cached in the dictionary, if yes then return it
    if n in cache:
        return cache[n]
    else:
        # cache/store the value in the dictionary and return the value for the input key
        cache[n] = getNthFib(n - 1, cache) + getNthFib(n - 2, cache)
        return cache[n]



# function call stack: https://www.youtube.com/watch?v=dxyYP3BSdcQ



#solve it iteratively
def getNthFib(n):
    lastTwoNum = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwoNum[0] + lastTwoNum[1]
        lastTwoNum[0] = lastTwoNum[1]
        lastTwoNum[1] = nextFib 
        counter += 1
    return lastTwoNum[1] if n > 1 else lastTwoNum[0]


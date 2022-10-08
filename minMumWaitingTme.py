# Time spending on reading question, coding, testing
# reading question:  1 min
# coding: 40 min
# test code successfully: 5 min

# thoughts:
# sort the array in ascending order
# iterate through the ordered array, start on the first query and add  its waitingtime to all rest queries
# repeat it until we reach at the end of this array
# O(nlogn) time | O(1) space
def monimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft
    return totalWaitingTime


#test code:
# queries = [3, 2, 1, 2, 6]
# def monimumWaitingTime(queries):
# queries.sort()
# totalWaitingTime = 0
# for idx, duration in enumerate(queries):
#     print(idx)
#     print(duration)
#     queriesLeft = len(queries) - (idx + 1)
#     print(queriesLeft)
#     totalWaitingTime += duration * queriesLeft
    # return totalWaitingTime
    # print(totalWaitingTime)

# 1， 2， 2， 3， 6  # 0  1  1+2  1+2+2  1+2+2+3
# idx duration
#  0    1
#  1    2
#  2    2
#  3    3
#  4    6
# 1) 4 = 0+1*4   1 gets added by 4 times since there are 4 queries left in the array
# 2) 10 = 4+2*3
# 3) 14 = 10+2*2
# 4) 17 = 14+3*1


#updated solution by using recursion
def minimumWaitingTime(queries):
    queries.sort()
    return recursion(queries)
def recursion(queries):
    if queries == []:
        return False
    return sum(queries[:-1]) + recursion(queries[:-1])


#####################################################################
# Date: 10/31/2022
# Author: Fary
# Problems solved: 3
# Difficulty Level: easy
#####################################################################
# problem1
# reading question:1m
# thoughts:
# recursively traverse the binary tree using depth-first-search
# pass sum of the values of all previously visited nodes to the current node that we are traversing
# O(n) time | O(1) space



# problem2: Tandem Bicycle
# reading question: 5m
# notes:
# tandem speed = max(A, B)
# maximum total tandem speed
# minimum total tandem speed
# thoughts:
# sort both arrays in ascending order, if fastest is true, get maximum total speed by using 2 pointers
# otherwise, reverse one of the sorted array to get minimum total speed
# O(nlogn) time | O(1) space



# problem3: Class Photos
# reading question: 3m
# notes: A is strictly taller than B
# thoughts:
# sort 2 arrays in descending order
# place the tallest student in the back row, if it's in blue color shirt, place students in blue in the back row, students in red in the front row
# check if each student in the back row can be paired with a student in the front row, if yes, return True, otherwise, return False
# O(nlogn) time | O(1) space







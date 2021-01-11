# twoSum
# This is a classic problem that tests your ability to itentify the time complexity of algorithms, and decide which implementation is better based on your assessment.

# Given an unsorted array of integers and a target, find the two integers in the array that sum up to the target, and return the indicies of those integers in the array. There will be exactly 1 combination that gives the correct sum, and you cannot use the same element twice. (So for example, twoSum([1,2,5], 10) -> [2, 2] is not valid.)

# Sample 1: twoSum([11, 2, 7, 15], 9) -> [1, 2]

# O(n^2)
def twoSum(arr, n):
    if len(arr) < 2: raise ValueError("Array cannot be less than two values")
    if len(arr) == 2: return [0,1] if arr[0] + arr[1] == n else []
    newArr = arr
    while len(newArr) > 0:
        val = n - arr[i]
        if val in set(arr[1:]): 
            #find the index, return
        newArr = newArr[1:]

# O(n)
def twoSum_faster(arr,n):
    return
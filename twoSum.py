# twoSum
# This is a classic problem that tests your ability to itentify the time complexity of algorithms, and decide which implementation is better based on your assessment.

# Given an unsorted array of integers and a target, find the two integers in the array that sum up to the target, and return the indicies of those integers in the array. There will be exactly 1 combination that gives the correct sum, and you cannot use the same element twice. (So for example, twoSum([1,2,5], 10) -> [2, 2] is not valid.)

# Sample 1: twoSum([11, 2, 7, 15], 9) -> [1, 2]

# O(n)
def twoSum(arr,n):
    val_dict = {}
    for i in range(len(arr)): val_dict[str(arr[i])] = i
    for key, index in val_dict.items():
        val = str(n - int(key))
        if val in val_dict and index != val_dict[val]: 
            return[index, val_dict[val]]
    return []

assert(twoSum([11,2,7,15], 9) == [1,2])
# Intersection of two arrays
# Another classic!

# Given two arrays of integers, return an array that contains just the elements that are present in both input arrays. The input arrays are not guaranteed to be sorted, but any given element will only appear once in a given input array.

# Sample 1: intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]) -> [0, 4]

#assume all intgers
def intersection(n,m):
    # empty arrays
    if len(n) == 0 or len(m) == 0: return []
    intersect = []
    for i in range(len(n)):
        if n[i] in set(m): intersect.append(n[i])
    return intersect

assert(intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]) == [0, 4])
assert(intersection([0, 1, 2, 3, 8], [0, 2, 7, 9, 4]) == [0, 2])
assert(intersection(['cat', 'apple', 'rabbit'], ['orange', 'banana', 'frog', 'cat']) == ['cat'])
assert(intersection([0, 1, 4, 5, 8], []) == [])
    
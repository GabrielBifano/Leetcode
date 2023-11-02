# Unique Number of Occurrences
# Easy

from collections import Counter

def uniqueOccurrences(arr: 'list[int]') -> bool:

    occur = Counter(arr)
    hash = [0]*len(arr)

    for key in occur:
        hash[occur[key]-1] += 1
        if hash[occur[key]-1] > 1:
            return False
    return True
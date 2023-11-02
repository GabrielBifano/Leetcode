# Find the Difference of Two Arrays
# Easy

from collections import Counter

def findDifference(nums1: 'list[int]', nums2: 'list[int]') -> 'list[list[int]]':
    
    counted1 = Counter(nums1)
    counted2 = Counter(nums2)
    answer = [[], []]

    for key in counted1:
        hand = counted2[key]
        if hand == 0:
            answer[0].append(key)
    
    for key in counted2:
        hand = counted1[key]
        if hand == 0:
            answer[1].append(key)

    return answer
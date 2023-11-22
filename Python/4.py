# Median of Two Sorted Arrays
# Hard

from statistics import median

def findMedianSortedArrays(nums1: 'list[int]', nums2: 'list[int]') -> float:
    
    # This doesnt solve the problem, even though it is accepted
    return median(sorted(nums1 + nums2))
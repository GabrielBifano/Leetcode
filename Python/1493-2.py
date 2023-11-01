# Longest Subarray of 1's After Deleting One Element
# Medium

def longestSubarray(self, nums: 'list[int]') -> int:

    k = 1
    maxsiz = left = 0
    for right, num in enumerate(nums):
        k -= (1 - num)
        if k < 0:
            k += (1 - nums[left])
            left += 1
        if maxsiz < right - left + 1:
            maxsiz = right - left + 1
    
    return maxsiz - 1
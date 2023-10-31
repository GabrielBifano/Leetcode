# Max Consecutive Ones III
# Medium

def longestOnes(nums: 'list[int]', k: int) -> int:
    
    maxsiz = left = 0
    for right, num in enumerate(nums):
        k -= (1 - num)
        if k < 0:
            k += (1 - nums[left])
            left += 1
        if maxsiz < right - left + 1:
            maxsiz = right - left + 1
    
    return maxsiz
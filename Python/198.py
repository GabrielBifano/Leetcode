# House Robber
# Medium

from functools import lru_cache

def rob(nums: 'list[int]') -> int:
    
    @lru_cache
    def help(i: int):
        if i == 0:
            return nums[0]
        elif i == 1: 
            return max(nums[0], nums[1])
        else: 
            return max(nums[i] + help(i-2), help(i-1))
    
    return help(len(nums) - 1)
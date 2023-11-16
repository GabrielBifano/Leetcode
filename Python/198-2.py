# House Robber
# Medium

def rob(nums: 'list[int]') -> int:
    
    cache = {}
    cache[0] = nums[0]
    
    def help(i: int):
        if i in cache:
            return cache[i]
        elif i == 1: 
            cache[1] = max(nums[0], nums[1])
            return cache[1]
        else: 
            cache[i] = max(nums[i] + help(i-2), help(i-1))
            return cache[i]
    
    return help(len(nums) - 1)
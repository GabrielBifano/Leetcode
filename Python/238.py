# Product of Array Except Self
# Medium

def productExceptSelf(nums: 'list[int]') -> 'list[int]':
    
    cumulative_prefix = 1
    cumulative_suffix  = 1

    siz = len(nums)
    mul_values = [0]*siz
    for i in range(siz):
        mul_values[i] = cumulative_prefix
        cumulative_prefix *= nums[i]
    
    for i in range(siz - 1, -1, -1):
        mul_values[i] *= cumulative_suffix
        cumulative_suffix *= nums[i]
    
    return mul_values

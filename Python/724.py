# Find Pivot Index
# Easy

def pivotIndex(nums: 'list[int]') -> int:

    prefix, suffix = 0, 0
    siz = len(nums)
    if siz == 1: return 0
    right, left = [], []

    for i in range(siz):
        prefix += nums[i]
        left.append(prefix)
    
    for i in range(siz - 1, -1, -1):
        suffix += nums[i]
        right.append(suffix)
    
    for i in range(siz):
        if i == 0:
            print(f'at index {i} --> {right[siz - i - 2]}')
            if right[siz - i - 2] == 0: return i
        elif i == siz - 1:
            if left[i - 1] == 0: return i
        else:
            if right[siz - i - 2] == left[i - 1]: return i

    return -1
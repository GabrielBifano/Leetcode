# Longest Subarray of 1's After Deleting One Element
# Medium

def longestSubarray(self, nums: 'list[int]') -> int:

    if len(nums) == 0: return 0
    maxsiz = siz = 0
    i = j = 0
    k = 1

    while j < len(nums):
        if nums[j] == 0:
            if k > 0:
                j += 1
                siz += 1
                k -= 1
            else:
                for t in range(i, j+1):
                    siz -= 1
                    if nums[t] == 0:
                        k += 1
                        i = t + 1
                        break
        else:
            j += 1
            siz += 1
        
        if maxsiz < siz:
            maxsiz = siz
    
    return maxsiz - 1
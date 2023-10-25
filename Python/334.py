# Increasing Triplet Subsequence
# Medium

class Solution:
    def increasingTriplet(self, nums: 'list[int]') -> bool:
        f = s = 2147483648
        for i in nums:
            if i > s:
                return True
            elif i <= f:
                f = i
            else:
                s = i
        return False
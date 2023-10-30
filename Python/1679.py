# Max Number of K-Sum Pairs
# Medium

from collections import Counter

def maxOperations(nums: 'list[int]', k: int) -> int:
    ops = 0
    c = Counter(nums)
    seen = set()

    for num in nums:
        if num not in seen and (k - num) in c:
            seen.add(num)
            if num == k - num:
                ops += c[num] // 2
                continue
            ops += min(c[num], c[k - num])
            seen.add(k - num) 

    return ops 
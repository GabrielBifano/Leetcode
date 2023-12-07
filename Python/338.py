# Counting Bits
# Easy

def countBits(n: int) -> 'list[int]':
    ans = []
    for i in range(n + 1):
        ones = 0
        while i > 0:
            if i >> 1 << 1 < i:
                ones += 1
            i = i >> 1
        ans.append(ones)
    return ans
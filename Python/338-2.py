# Counting Bits
# Easy

def countBits(n: int) -> 'list[int]':
    ans = [0]
    for i in range(1, n + 1):
        ans.append(ans[int(i/2)] + i%2)
    return ans
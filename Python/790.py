# Domino and Tromino Tiling
# Medium

class Solution:
    def numTilings(self, n: int) -> int:
        A = [1, 1, 2]
        for i in range(3, n + 1):
            A.append(2*A[i-1] + A[i-3])
        return A[n] % 1_000_000_007
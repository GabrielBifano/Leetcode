# N-th Tribonacci Number
# Easy

from functools import lru_cache

@lru_cache
def tribonacci(n: int) -> int:
    if n == 0: return 0
    elif n <= 2: return 1
    else:
        return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
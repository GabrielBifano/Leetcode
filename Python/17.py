# Letter Combination of a Phone Number
# Medium

from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> 'list[str]':
        keyboard = {
            '2': 'abc','3': 'def',
            '4': 'ghi','5': 'jkl',
            '6': 'mno','7': 'pqrs',
            '8': 'tuv','9': 'wxyz',
        }
        if digits == "": return []
        strs = [keyboard[c] for c in digits]
        return [''.join(comb) for comb in product(*strs)]
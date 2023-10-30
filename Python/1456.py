# Maximum Number of Vowels in a Substring of Given Length
# Medium

def maxVowels(s: str, k: int) -> int:
    
    dt = {
        'a': 1,
        'e': 1,
        'i': 1,
        'o': 1,
        'u': 1,
    }

    ls = [dt.get(x, 0) for x in s]
    max_vowels = sum(ls[0:k])
    sum_vowels = max_vowels
    for i in range(1, len(ls) - k + 1):
        j = i + k - 1
        sum_vowels = sum_vowels - ls[i - 1] + ls[j]
        if max_vowels < sum_vowels:
            max_vowels = sum_vowels
    return max_vowels
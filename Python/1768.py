# Merge Strings Alternately
# Easy

def mergeAlternately(word1: str, word2: str) -> str:
    
    res = ""
    i = 0

    while i < len(word1) and i < len(word2):
        res += word1[i]
        res += word2[i]
        i += 1
    res += word1[i:]
    res += word2[i:]

    return res
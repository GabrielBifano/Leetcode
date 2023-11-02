# Determine if Two Strings Are Close
# Medium

from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:

    if len(word1) != len(word2): return False

    w1 = Counter(word1)
    w2 = Counter(word2)
    if len(w1) != len(w2): return False

    for key in w1:
        if w2[key] == 0:
            return False

    v1 = sorted(w1.values())
    v2 = sorted(w2.values())

    for i in range(len(v1)):
        if v1[i] != v2[i]: return False
    
    return True

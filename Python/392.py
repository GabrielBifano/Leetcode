# Is Subsequence
# Easy

def isSubsequence(s: str, t: str) -> bool:

    subseq_char = 0
    subseq_size = len(s)
    if subseq_size == 0: return True

    for letter in t:
        if letter == s[subseq_char]:
            subseq_char += 1
            if subseq_char == subseq_size:
                return True
    return False
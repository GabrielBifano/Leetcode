# Reverse Vowels of a String
# Easy

def reverseVowels(s: str) -> str:
        
    posivec = []
    vowels  = []
    for i in range(len(s)):
        c = s[i]
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            posivec.append(i)
            vowels.append(c)
    
    siz = len(vowels)
    for i in range(siz):
        pos = posivec[siz - i - 1]
        s = s[:pos] + vowels[i] + s[pos + 1:]

    return s
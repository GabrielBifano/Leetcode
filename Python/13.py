#
# Easy

def romanToInt(s: str) -> int:
    alph = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    num = 0
    for i in range(len(s) - 1):
        
        this = alph[s[i]]
        next = alph[s[i + 1]]

        if this < next:
            num -= this
        else: num += this

    return num + alph[s[-1]]
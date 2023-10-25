# Greatest Common Divisor of Strings
# Easy

def gcdOfStrings(str1: str, str2: str) -> str:

    def isGCD(string: str, substr: str):  
        if len(string.replace(substr, '')) > 0:
            return False
        return True
    
    def computeGCD(a, b):
        cd = []
        for i in range(1, min(a, b) + 1):
            if a%i == b%i == 0:
                cd.append(i)
        return cd

    siz_1, siz_2 = len(str1), len(str2)
    cd = computeGCD(siz_1, siz_2)
    for divisor in reversed(cd):
        prefix = str1[:divisor]
        if isGCD(str2, str1[:divisor]) and isGCD(str1, str2[:divisor]):
            return prefix
    return ""
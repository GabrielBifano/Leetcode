def decodeString(s: str) -> str:

    def get_nums(s):
        n = len(s) - 1
        number, i = "", 0
        while i < n:
            char = s[i]
            if char.isdigit():
                number = number + char
            elif char == '[':
                if number:
                    yield int(number)
                    number = ""
            i += 1

    opens = [i for i, x in enumerate(s) if x == '[']
    numbs = [i for i in get_nums(s)]

    while len(opens) > 0:
    
        i = opens.pop()
        k = numbs.pop()

        cindex = 0
        for j in range(i, len(s)):
            if s[j] == ']':
                cindex = j
                break

        s = s[:i-len(str(k))] + k * s[i + 1: cindex] + s[cindex + 1:]
    
    return s
# Removing Stars From a String
# Medium

from collections import deque

def removeStars(s: str) -> str:
    
    stars = 0
    st = deque()

    for i in range(len(s)-1, -1, -1):
        char = s[i]
        if char == '*':
            stars += 1
        elif stars == 0:
            st.appendleft(char)
        else:
            stars -= 1

    return ''.join(st)
# Reverse Words in a String
# Medium

def reverseWords( s: str) -> str:
        words = []
        word = ""
        for letter in s:
            if letter != " ":
                word += letter
            elif len(word) > 0:
                words.append(word)
                word = ""
        if len(word) > 0:
            words.append(word)
        
        answer = ""
        for w in reversed(words):
            answer += w + ' '
        answer = answer[:-1]
        return answer
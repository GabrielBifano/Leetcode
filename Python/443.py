def compress(chars: 'list[str]') -> int:

        sentence = "".join(chars)
        store = []
        store_siz = 0
        while len(sentence) > 0:
            size_before = len(sentence)
            char = sentence[0]
            sentence = sentence.lstrip(char)
            diff = size_before - len(sentence)
            store.append((char, diff))
            store_siz += 1 + len(str(diff))
        
        j = 0
        for char, reps in store:
            chars[j] = char
            if reps > 1:
                for alg in str(reps):
                    j += 1
                    chars[j] = alg
            j += 1

        return store_siz
    
print(compress(["a","a","b","b","c","c","c"]))
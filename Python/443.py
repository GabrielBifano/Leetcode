# String Compression
# Medium

def compress(chars: 'list[str]') -> int:

    sentence = "".join(chars)
    buff = []
    buffsiz = 0

    while len(sentence) > 0:
        # saves old str length
        length = len(sentence)

        # apply lstrip
        sentence = sentence.lstrip(sentence[0])
        
        # get the repetitions of first character
        diff = length - len(sentence)

        # store the character and its repetitions
        buff.append((sentence[0], diff))

        # updates the space that buff will occupy later in chars
        buffsiz += 1 + len(str(diff)) * (diff > 1)
    
    # write buff to chars
    j = 0
    for char, reps in buff:
        chars[j] = char
        if reps > 1:
            for alg in str(reps):
                j += 1
                chars[j] = alg
        j += 1
    
    return buffsiz
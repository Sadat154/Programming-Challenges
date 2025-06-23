def mergeAlternatively(word1, word2):
    merged = []
    for a, b in zip(word1, word2):
        merged.append(a+b)


    merged.extend(word1[len(word2):])
    merged.extend(word2[len(word1):])

    return ''.join(merged)


print(mergeAlternatively("hello", "world"))
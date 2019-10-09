def wordsTyping(sentence, rows, cols):
    cols_left = cols
    comb_string = ' '.join(sentence)
    sentence_len = len(sentence)
    res = 0
    for i in range(rows):
        res += cols
        while res > 0 and sentence[res % sentence_len] != ' ':
            res -= 1
        if sentence[res % sentence_len] == ' ':
            res += 1
    return res // sentence_len


print(wordsTyping(["try", "to", "be", "better"],
                  10000,
                  9001))

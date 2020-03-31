
# repeated words

import re
words = "the cat is a cat where the cat is not a dog, but a animal."


def num_repeated_words(words):
    result = re.findall('[A-Za-z]+', words)
    print(result)
    res = 0
    Set = {}
    for word in result:
        if word in Set and not Set[word]:
            res += 1
            Set[word] = 1
        else:
            Set[word] = 0
    return res


print(num_repeated_words(words))

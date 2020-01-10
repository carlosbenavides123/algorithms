# create all possible words given a phone number

mappings = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def phone_words(phone_number):
    res = []
    word = ""
    recurse(0, word, res, phone_number)
    return res

def recurse(digit, word, res, phone_number):
    if len(phone_number) == digit:
        res.append(word)
    else:
        for c in mappings[int(phone_number[digit])]:
            word += c
            recurse(digit+1, word, res, phone_number)

print(phone_words("11433258"))
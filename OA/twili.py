def segments(message):
    if len(message) <= 160: return [message]
    result = []
    space = 0
    start = 0
    end = 154

    while end < len(message):
        while (end > start and message[end]!= " " and message[end + 1]!= " "):
            end -= 1
        result.append(message[start:end+1])
        start = end + 1
        if space <= 5:
            end = start + 154
        else:
            end = start + 159
        space +=1
    result.append(message[start:end+1])
    space += 1
    for i in range(space):
        result[i] += "(" + str(i+1) + "/" + str(space) + ")"
    return result


class Trie():
    def __init__(self):
        self.trie = {}

    def add_word(self, word):
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] = word
 
    # use after_first_valid as a number after search
    # so for example if we have codes -> 8943, 9432
    # and if we have number +18932xxxx
    # this algo will fail because it would be expecting sequence 8943 and not 9432
    # overall, a simple backtrack if needed
    def search_word(self, phone_number):
        curr = self.trie
        i = 0
        last_valid = 0
        after_first_valid = None
        while i < len(phone_number):
            letter = phone_number[i]
            if letter in curr:
                # hold this state for backtracking
                if not after_first_valid:
                    after_first_valid = i
                curr = curr[letter]
                if "*" in curr: return True
            else:
                # backtrack
                curr = self.trie
                if after_first_valid and phone_number[after_first_valid] in curr:
                    i = after_first_valid
                    after_first_valid = None
                else:
                    if letter in curr:
                        curr = curr[letter]
            i += 1
        if "*" in curr: return True
        return False

hash_map = {
    "a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3, "g": 4, "h": 4, "i": 4, "j": 5, "k": 5, "l": 5,
    "m": 6, "n": 6, "o": 6, "p": 7, "q": 7, "r": 7, "s": 7, "t": 8, "u": 8, "v": 8, "w": 9, "x": 9, "y": 9, "z":9
}

def vanity(codes, numbers):
    trie = Trie()
    # create combos
    combos = []
    for code in codes:
        combo = ""
        for letter in code:
            combo += str(hash_map[letter.lower()])
        combos.append(combo)
    # make trie
    for combo in combos:
        trie.add_word(combo)

    # use set because of duplicates
    res = set()
    for number in numbers:
        if trie.search_word(number):
            res.add(number)

    return sorted(list(res))

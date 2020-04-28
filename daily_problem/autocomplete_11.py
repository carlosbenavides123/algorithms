# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s
# and a set of all possible query strings, return all strings in the set 
# that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], 
# return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to 
# speed up queries.

string = input()
words = [str(x) for x in input().split(" ")]

class Trie():
    def __init__(self):
        self.root = {}
    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] = {}
        
    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
            if "*" in curr:
                return True
        return False

def solve(search_string, words):
    trie = Trie()
    trie.add_word(string)
    res = []
    for word in words:
        if trie.search(word):
            res.append(word)
    return res
print(solve(string, words))

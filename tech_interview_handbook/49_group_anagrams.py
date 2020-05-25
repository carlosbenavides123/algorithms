#Given an array of strings, group anagrams together.

#Example:

#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

def solve(words):
    res = {}
    for word in words:
        tp = generate_tuple(word)
        if tp in res:
            res[tp].append(word)
        else:
            res[tp] = [word]
    return [val for key,val in res.items()]
def generate_tuple(word):
    char_arr = [0] * 26
    for letter in word:
        char_arr[ord(letter) - ord('a')] += 1
    return tuple(char_arr)
print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
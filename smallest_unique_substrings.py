# Input: ["cheapair", "cheapoair", "peloton", "pelican"]
# Output:
# "cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
# "cheapoair": "po" // "oa" would also be acceptable
# "pelican": "ca"   // "li", "ic", or "an" would also be acceptable
# "peloton": "t"    // this single letter doesn't occur in any other string

import collections
class Trie:
    def __init__(self):
        self.root = self
        self.children = collections.defaultdict(Trie)
        self.root_word = ""
        self.substring = ""
        self.belongs_to = set()

    def add_word(self, word):
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                curr = self.root
                substring = word[i:j]
                curr = curr.children[substring]
                curr.belongs_to.add(word)

    def find_substring(self, word):
        res = word
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                curr = self.root
                sub_string = word[i:j]
                curr = curr.children[sub_string]
                if word in curr.belongs_to and len(curr.belongs_to) > 1: continue
                # print(sub_string, word)
                res = min(sub_string, res, key=len)
        return res

    # def print_trie(self):
        # q = collections.deque()
        # q.append(self.root.children)
        # while q:
        #     node = q.popleft()
        #     # print(node.root_word)
        #     for key, value in node.items():
        #         print(key, value.root_word)

def smallest_unique_substrings(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)
    # print(trie.children.keys())
    temp_res = {}
    for word in words:
        temp_res[word] = trie.find_substring(word)
    return temp_res


print(smallest_unique_substrings(["cheapair", "cheapoair", "peloton", "pelican"]))

# def brute_force(words):
#     res = {}
#     for word in words:
#         res[word] = word
#         for i in range(len(word)):
#             for j in range(i + 1, len(word)):
#                 sub_string = word[i:j]
#                 for word_2 in words:
#                     if word_2 == word: continue
#                     if sub_string in word_2: break
#                 else:
#                     if len(sub_string) < len(res[word]):
#                         res[word] = sub_string
#     return res
# print(brute_force(["cheapair", "cheapoair", "peloton", "pelican"]))

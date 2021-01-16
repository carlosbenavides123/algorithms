# Given an array of words, return the length of the longest phrase, containing only unique characters, that you can form by combining the given words together.

# words = ["the","dog","ran"], return 9 because you can combine all the words, i.e. "the dog ran" since all the characters in the phrase are unique.
# Ex: Given the following words…

# words = ["the","eagle","flew"], return 4 because "flew" is the longest phrase you can create without using duplicate characters.

def longest_phrase(words):
    res = [""]
    backtrack_longest_phrase(words, 0, "", res)
    return res[0]

def backtrack_longest_phrase(words, curr_idx, s, res):
    if curr_idx == len(words):
        return

    for i in range(curr_idx, len(words)):
        curr_word = words[i]
        if len(s + curr_word) == len(set(s + curr_word)):
            res[0] = max(res[0], s + curr_word, key=len)
            backtrack_longest_phrase(words, i + 1, s + curr_word, res)

words = ["the", "dog", "ran"] # the dog ran
print(longest_phrase(words))
words = ["the", "eagle", "flew"]
print(longest_phrase(words)) # flew
words = ["dog", "eagle", "flew"]
print(longest_phrase(words)) # flew

words = ["opxzvasre", "nm", "the", "dog", "ran"]
print(longest_phrase(words)) # flew

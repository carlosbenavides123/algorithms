# 3. Longest Substring Without Repeating Characters
# Medium

# 7181

# 424

# Add to List

# Share
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a


def longest_substring(string):
    res = start = 0
    dic = {}
    for i in range(len(string)):
        char = string[i]
        if char in dic:
            start = max(start, dic[char] + 1)
        res = max(res, i - start + 1)
        dic[char] = i
    return res


print(longest_substring("abcabcbb"))

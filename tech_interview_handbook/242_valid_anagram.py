#Given two strings s and t , write a function to determine if t is an anagram of s.
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true

#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#Note:
#You may assume the string contains only lowercase alphabets.

#Follow up:
#What if the inputs contain unicode characters? How would you adapt your solution to such case?

# 26 letters in alphabet
# anagrams are just a string of the same length, using the same amount of characters
# make sure s, t are non null
# make sure len(s) == len(t)
# then use a character array for both s, t, compare the amount of characters x in each
# they should equal eachother i.e. s = 'aaa' t = 'aaa' s_char_arr[0] = 3 t_char_arr[0] = 3
# use algorith curr_letter - 'a'

# o n time o 1 space
def solve(s, t):
    if not s or not t:
        return False
    if len(s) != len(t):
        return False
    s_char_arr = [0] * 26
    t_char_arr = [0] * 26
    
    for letter in s:
        s_char_arr[ord(letter) - ord('a')] += 1
    for letter in t:
        t_char_arr[ord(letter) - ord('a')] += 1
    
    for i in range(26):
        if s_char_arr[i] != t_char_arr[i]:
            return False
    return True
s = "anagram"
t = "nagaram"
print(solve(s, t))
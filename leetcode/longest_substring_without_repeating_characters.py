# title

string = input("longest string")

def longest_string(s):
    seen = {}
    res = 0
    start_of_string = 0
    for i in range(len(s)):
        letter = s[i]
        if letter in seen:
            start_of_string = max(start_of_string, seen[letter] + 1)
        res = max(res, i - start_of_string + 1)
        seen[letter] = i
    return res
print(longest_string(string))
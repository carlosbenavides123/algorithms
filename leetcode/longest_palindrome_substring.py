#title

string = input("input string \n")

def longest_palindrome(s):
    if len(s) <= 1:
        return s
    res = ""
    for i in range(1, len(s)):
        res = max(expand(i-1, i, s), res, key=len)
        res = max(expand(i-1, i+1, s), res, key=len)
    return res
def expand(l, r, s):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

print(longest_palindrome(string))
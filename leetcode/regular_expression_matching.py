# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, 
# a can be repeated 1 time. Therefore, it matches "aab".

s = input()
p = input()

def match(s, p):
    if not p:
        return not s
    first_letter_match = s and (s[0] == p[0] or p[0] == ".")
    
    if len(p) >= 2 and p[1] == "*":
        return (first_letter_match and match(s[1:], p[:])) or match(s, p[2:])
    else:
        return first_letter_match and match(s[1:], p[1:])
print(match(s, p))

def match(s, p):
    dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i-1] == "*":
            dp[0][i] = dp[0][i-2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i-1] == p[j-1] or p[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                if dp[i][j-2] or (dp[i-1][j] and p[j-2] in [".", s[i-1]]):
                    dp[i][j] = True
            else:
                dp[i][j] = False
    return dp[-1][-1]

print(match(s, p))
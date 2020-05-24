#This problem was asked by Facebook.

#Implement regular expression matching with the following special characters:

#. (period) which matches any single character
#* (asterisk) which matches zero or more of the preceding element
#That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

#For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

#Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

reg = input() # "ra." ".*at"
match = input() # "ray" "chat"

# rec
def solve(reg, match):
    if not match:
        return not reg
    
    first_match = reg and (reg[0] == "." or reg[0] == match[0])
    
    if len(reg) >= 2 and reg[1] == "*":
        return first_match and solve(reg, match[1:]) or (first_match and solve(reg[2:], match))
    return first_match and solve(reg[1:], match[1:])

print(solve(reg, match))

# dp
def solve(reg, match):
    dp = [[False for y in range(len(reg) + 1)] for x in range(len(match) + 1)]
    dp[0][0] = True
    # .*at
    # chat
    #     . * a t
    #   t f f f f
    # c f t t f f
    # h f t f f f
    # a f t f t f
    # t f t f f t
    
    for i in range(1, len(dp)):
        m = match[i-1]
        for j in range(1, len(dp[0])):
            p = reg[j-1]
            if p == "." or p == m:
                dp[i][j] = True
            elif p == "*":
                dp[i][j] = dp[i-1][j-2]
    for row in dp:
        print(row)
    return dp[-1][-1]
print(solve(reg, match))

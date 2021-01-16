# This problem was asked by YouTube.

# Write a program that computes the length of the longest common subsequence of three given strings.
# For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
# it should return 5, since the longest common subsequence is "eieio".


# two strings
# epidemiologist
# refrigeration

a = "epidemiologist"
b = "refrigeration"

def lcs(a, b):
    dp = [[0 for y in range(len(b) + 1)] for x in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

print(lcs(a, b))

# three strings

a = "epidemiologist"
b = "refrigeration"
c = "supercalifragilisticexpialodocious"

# def lcs(a, b, c):
#     dp = [[[0 for k in range(len(c) + 1)] for j in range(len(b) + 1)] for i in range(len(a) + 1)]

#     for i in range(1, len(a) + 1):
#         for j in range(1, len(b) + 1):
#             for k in range(1, len(c) + 1):
#                 if a[i-1] == b[j-1] == c[k-1]:
#                     dp[i][j][k] = dp[i-1][j-1][k-1] + 1
#                 else:
#                     dp[i][j][k] = max(dp[i][j-1][k-1], dp[i-1][j][k-1], dp[i-1][j-1][k])
#     return dp[-1][-1][-1]
# print(lcs(a, b, c))

def lcs(a, b, c):
    dp = [[[0 for k in range(len(c) + 1)]
                for j in range(len(b) + 1)]
                for i in range(len(a) + 1)]

    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if a[i] == b[j] == c[k]:
                    dp[i+1][j+1][k+1] = dp[i][j][k] + 1
                else:
                    dp[i+1][j+1][k+1] = max(
                            dp[i][j + 1][k + 1],
                            dp[i + 1][j][k + 1],
                            dp[i + 1][j + 1][k]
                            )
    return dp[-1][-1][-1]
print(lcs(a, b, c))

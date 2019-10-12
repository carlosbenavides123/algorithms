# Given two strings, determine the edit distance between them.
# The edit distance is defined as the minimum number of edits
# (insertion, deletion, or substitution) needed to change one string
# to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

# Here's the signature:


def distance(s1, s2):
    # Fill this in.
    dp = [[0 for y in range(len(s2)+1)] for x in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + 1
                )
    for x in range(len(dp)):
        print(dp[x])
    return dp[-1][-1]


print distance('biting', 'sitting')
# 2

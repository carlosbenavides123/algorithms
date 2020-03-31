# 64. Minimum Path Sum
# Medium

# 2065

# 48

# Add to List

# Share
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
# sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1->3->1->1->1 minimizes the sum.

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


def minPathSum(grid):
    res = float("inf")
    dfs(res, grid, 0, 0, 0)
    return res


def dfs(res, grid, curr, i, j):
    # if grid[i][j] == -1:
    #     return
    if i == len(grid) and j == len(grid[0]):
        res = min(res, curr)
        print(res)
        return
    else:
        # print(grid[i][j], currs)
        curr += grid[i][j]
        # temp = grid[i][j]
        grid[i][j] = -1

        for other_x, other_y in [[0, 1], [1, 0]]:
            new_x, new_y = i + other_x, j + other_y

            if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]):
                if grid[new_x][new_y] == -1:
                    continue
                dfs(res, grid, curr, new_x, new_y)

        # grid[i][j] = temp
        # return


print(minPathSum(grid))

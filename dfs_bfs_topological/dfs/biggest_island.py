# number of islands
# leetcode medium

#given a matrix of 0's and 1's, determine the longest island

def big_island(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                res.append( dfs(i, j, matrix, 0) )
    return max(res) if res else 0

def dfs(x, y, matrix, count):
    count += 1
    matrix[x][y] = 0
    for other_x, other_y in [ [1, 0], [0, 1], [-1, 0], [0, -1] ]:
        new_x, new_y = x + other_x, y + other_y
        if -1 < new_x < len(matrix) and -1 < new_y < len(matrix[0]):
            if matrix[new_x][new_y]:
                count = dfs(new_x, new_y, matrix, count)
    return count

print(big_island(
    [
        [1, 0, 1, 0, 0],
        [1, 1, 0 , 1, 1],
        [1, 0, 1, 0, 1]
    ]
))
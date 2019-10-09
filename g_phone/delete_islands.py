# Given a binary grid where 0 represents water and 1 represents
# land. An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically.
# Delete all islands except their borders. A border is land
# adjacent to water. You may assume all four edges of the
# grid are surrounded by water.

# Just replace the ones want to delete with -1

# NO NEED FOR BFS/DFS


def delete_islands(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 1 and should_delete(grid, i, j):
                grid[i][j] = -1
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == -1:
                grid[i][j] = 0
    return grid


def should_delete(grid, x, y):
    for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
        next_x, next_y = i + x, j + y
        if not grid[next_x][next_y]:
            return False
    return True


print(delete_islands(

    [[0, 0, 0, 1, 1, 1],
     [0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]

))

def matrix_spiral_print(M):
    # Fill this in.
    u, d, l, r = 0, len(M) - 1, 0, len(M[0]) - 1
    while l < r and u < d:
        for j in range(l, r):
            print(M[u][j])
        for i in range(u, d):
            print(M[i][r])
        for j in range(r, l, -1):
            print(M[d][j])
        for i in range(d, u, -1):
            print(M[i][l])
        u, d, l, r = u + 1, d - 1, l + 1, r - 1

    # can also add...
    # if l == r:
    #     ans.extend([matrix[i][r] for i in xrange(u, d + 1)])
    # elif u == d:
    #     ans.extend([matrix[u][j] for j in xrange(l, r + 1)])


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print matrix_spiral_print(grid)

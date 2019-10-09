# Given a matrix of size m x n, there exists a square of all 1s
# in the matrix (all other entries in the matrix are 0s).
# The square of 1s is sqrt(n) or greater in size. Find the top
# left corner of the square and return the size of the square as well.

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
]

# ????????????


def matrix_of_ones(matrix):
    m = len(matrix)
    n = len(matrix[0])
    i, j = 0, 0
    while True:
        check_i, check_j = int(i * n ** 0.5), int(j * n ** 0.5)
        print(check_i, check_j)
        if check_i < n and check_j < m:
            if matrix[check_i][check_j] == 1:
                print(matrix[check_i][check_j])
                break
            else:
                i += 1
                j += 1
                continue
        else:
            break


print(matrix_of_ones(matrix))

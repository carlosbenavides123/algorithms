# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# 1 2 3
# 4 5 6
# 7 8 9
# 
# 7 4 1
# 8 5 2
# 9 6 3

# n x n matrix
def rotate_image(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
    for i in range(len(matrix)):
        for j in range( int(len(matrix[0]) / 2) ):
            matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
    print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_image(matrix))
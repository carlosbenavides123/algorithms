# Print a N x M matrix in diagonal from the upper left to lower right.
# However, with the following caveat.
# It's easy to just show the input and expect output.

# matrix:
# a b c
# d e f g
# h i j k

# output:
# aej
# bfk
# cg
# di
# h


def solution(matrix):
    # Set = set()
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         string = dfs(matrix, Set, i, j)
    #         if len(string) and string != " ":
    #             print(string)
    completed_half = False
    i = 0
    counter, matrix_len = 0, len(matrix) * len(matrix[0])
    while counter < matrix_len:
        max_range_to_search = 1 if completed_half else len(matrix[0])
        for j in range(max_range_to_search):
            build_string = ""
            i_pointer = i
            j_pointer = j
            print(i_pointer, j_pointer)
            while i_pointer < len(matrix) and j_pointer < len(matrix[0]):
                build_string += matrix[i_pointer][j_pointer]
                i_pointer += 1
                j_pointer += 1
                counter += 1
            print(build_string)
        i += 1
        completed_half = True


# def dfs(matrix, Set, x, y):
#     if matrix[x][y] in Set:
#         return ""
#     res = matrix[x][y]
#     Set.add(matrix[x][y])
#     for i, j in [[1, 1]]:
#         next_x, next_y = x + i, y + j

#         if -1 < next_x < len(matrix) and -1 < next_y < len(matrix[0]):
#             res += dfs(matrix, Set, next_x, next_y)
#     return res
matrix = [
    ["a", "b", "c", " "],
    ["d", "e", "f", "g"],
    ["h", "i", "j", "k"],
    ["l", "m", "n", "o"],
    ["p", "q", "r", "s"]
]

print solution(matrix)

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10


class NumMatrix(object):
    def __init__(self, matrix):
        self.d = matrix
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]

    def update(self, row, col, val):
        row = self.d[row]
        orig = row[col] - (row[col-1] if col else 0)
        for i in range(col, len(row)):
            row[i] += val - orig

    def sumRegion(self, row1, col1, row2, col2):
        out = 0
        for i in range(row1, row2+1):
            x = self.d[i][col2]
            y = self.d[i][col1-1] if col1 else 0
            out += (x - y)
        return out


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
sol = NumMatrix(matrix)

sol.sumRegion(2, 1, 4, 3)
sol.update(3, 2, 2)
sol.sumRegion(2, 1, 4, 3)

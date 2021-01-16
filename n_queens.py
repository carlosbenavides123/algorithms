# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

def n_queens(n):
    res = []
    table = [["." for y in range(n)] for x in range(n)]
    rows = [True] * n
    cols = [True] * n
    asc_diag = [True] * (2*n - 1)
    desc_diag = [True] * (2*n - 1)

    def validate_table(row, col, placed_queens, table):
        queen = 1
        for i in range(0, row):
            if queen > 1: return False
            if table[i][col] == "Q": queen += 1
        if queen > 1: return False
        for prev_queen in placed_queens:
            if abs(prev_queen[0] - row) == abs(prev_queen[1] - col): return False
        return True

    def place_queen(row, placed_queens, table):
        if row == n:
            res.append(["".join(row) for row in table])
            return
        for col in range(n):
            table[row][col] = "Q"
            print(row, col)
            print(asc_diag[row + col])
            print(desc_diag[row - col])
            if rows[row] and cols[col] and asc_diag[row + col] and desc_diag[row - col]:
                rows[row] = False
                cols[col] = False
                asc_diag[row + col] = False
                desc_diag[row-col] = False
                place_queen(row + 1, placed_queens, table)
                rows[row] = True
                cols[col] = True
                asc_diag[row + col] = True
                desc_diag[row - col] = True
            # if validate_table(row, col, placed_queens, table):
            #     placed_queens.append((row, col))
            #     place_queen(row + 1, placed_queens, table)
            #     placed_queens.pop()
            table[row][col] = "."

    place_queen(0, [], table)
    return res

print(n_queens(4))
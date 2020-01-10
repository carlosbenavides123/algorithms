def n_queens(n):
    def solve(row):
        if row == n:
            result.append(col_placement)
            return
        for col in range(n):
            if all( abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve(row + 1)
    result = []
    col_placement = [0] * n
    solve(0)
    return result


print(n_queens(4))

# Given a square matrix of size NxN, complete the latin square. 
# A Latin square is a square that contains N sets of numbers from 1 to N arranged tthat no such row or column contains the same number twice.

# [1, x, 3, 4]       [1, 2, 3, 4]
# [x, 1, 4, 3]  ->   [3, 4, 1, 2]
# [3, 4, x ,x]       [4, 3, 2, 1]
# [4, 3, 2, 1]       [2, 1, 4 ,3]

import collections

def latin_sq(matrix):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    n = len(matrix)
    q = collections.deque()
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != "x":
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
            else:
                q.append((r, c))
    recurse_place_num(matrix, q, rows, cols)
    return matrix

def recurse_place_num(matrix, q, rows, cols):
    if not q:
        return True
    r, c = q[0]
    n = len(matrix)
    nums = [str(i) for i in range(1, 1 + n)]
    for num in nums:
        if num in rows[r] or num in cols[c]: continue
        rows[r].add(num)
        cols[c].add(num)
        matrix[r][c] = num
        q.popleft()
        if recurse_place_num(matrix, q, rows, cols):
            return True
        q.appendleft((r, c))
        rows[r].discard(num)
        cols[c].discard(num)
        matrix[r][c] = "x"
    return False

def print_matrix(matrix):
    for l in matrix:
        print(l)

matrix = [ ["1", "x", "3", "4"], ["x", "1", "4", "3"], ["3", "4", "x" ,"x"], ["4", "3", "2", "1"] ]
print(print_matrix(latin_sq(matrix)))

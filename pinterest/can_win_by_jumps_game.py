# Youre given a board game which is a row of squares
# each labeled with an integer. This can be represented by a list, e.g.

# [1, 3, 2, 0, 5, 2, 8, 4, 1]

# Given a start position on the board, you "win" by landing on a zero,
# where you move by jumping from square to square either
# left or right the number of spaces specified on the square youre currently on

# Your task is to implement the function:

# def can_win(board, pos): returns True if you can win the board from that starting pos, False otherwise

# this question was annoying
import collections
ip = [1, 3, 2, 0, 5, 2, 8, 4, 1]


def can_win(board, pos):
    g = collections.defaultdict(set)
    index = 0
    while index < len(board):
        if index == 0:
            create_graph_right(g, board, index)
            index += 1
            continue
        if index == len(board) - 1:
            create_graph_left(g, board, index)
            index += 1
            continue
        create_graph_left(g, board, index)
        create_graph_right(g, board, index)
        index += 1
    return dfs(g, pos, board, set())


def dfs(g, index, board, Set):
    if board[index] == 0:
        return True
    Set.add(index)
    if index in g:
        for other_idx in g[index]:
            if other_idx not in Set:
                if dfs(g, other_idx, board, Set):
                    return True
    return False


def create_graph_right(g, board, index):
    temp_idx = board[index] + index
    i = index
    while i + 1 < len(board) and i < temp_idx:
        g[index].add(i+1)
        i += 1


def create_graph_left(g, board, index):
    temp_idx = board[index]
    i = index
    count = 0
    while i - 1 > -1 and count < temp_idx:
        g[index].add(i-1)
        i -= 1
        count += 1


print(can_win(ip, 2))

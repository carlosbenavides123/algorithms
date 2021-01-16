# This question is asked by Facebook. Given an undirected graph determine whether it is bipartite.
# Note: A bipartite graph, also called a bigraph, is a set of graph vertices decomposed into two disjoint sets such that no two graph vertices within the same set are adjacent.

# Ex: Given the followinig graph...

# graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
# 0----1
# |    |
# |    |
# 3----2
# return true.
# Ex: Given the followinig graph...

# graph = [[1, 2], [0, 2, 3], [0, 1, 3], [0, 2]]
# 0----1
# |  / |
# | /  |
# 3----2
# return false.

import collections

def coloring(graph):
    colors = [-1] * len(graph)
    for i in range(len(graph)):
        if colors[i] == -1:
            colors[i] = 0
            stk = [i]

            while stk:
                curr_node = stk.pop()
                for neighbor_node in graph[curr_node]:
                    if colors[neighbor_node] == -1:
                        stk.append(neighbor_node)
                        colors[neighbor_node] = colors[curr_node] ^ 1
                    elif colors[neighbor_node] == colors[curr_node]:
                        return False
    return True

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(coloring(graph))
graph = [[1, 2], [0, 2, 3], [0, 1, 3], [0, 2]]
print(coloring(graph))

# leetcode medium
# given a int n, num of edges
# and a list of edges
# return the number of graphs

# IP n=5, edges = [ [0, 1], [1, 2], [3, 4] ]
# 0 -> 1 -> 2, 3 -> 4
# OP 2

def number_of_graphs(n, edges):
    res = 0
    import collections
    g = collections.defaultdict(set)
    for start, end in edges:
        g[start].add(end)

    visited = set()
    for i in range(n):
        if not i in visited:
            res += 1
            dfs(g, i, visited)
    return res

def dfs(g, key, visited):
    if key in visited:
        return
    visited.add(key)
    if key in g:
        for other_key in g[key]:
            dfs(g, other_key, visited)
    return
print(number_of_graphs(5, [ [0, 1], [1, 2], [3, 4] ]))
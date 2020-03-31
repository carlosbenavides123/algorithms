# 261. Graph Valid Tree
# Medium

import collections


def validTree(n, edges):
    if n - 1 != len(edges):
        return False
    g = collections.defaultdict(list)

    for edge1, edge2 in edges:
        g[edge1].append(edge2)
        g[edge2].append(edge1)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for other_node in g[node]:
            if other_node not in visited:
                if dfs(other_node, node):
                    return True
            elif other_node != parent:
                return True
        return False

    dfs(0, -1)
    return len(visited) == n


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(validTree(n, edges))

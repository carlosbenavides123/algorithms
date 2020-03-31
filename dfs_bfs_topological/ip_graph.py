
ips = [
    ["1.1.1.1", "2.2.2.2", 100],
    ["1.1.1.1", "3.3.3.3", 200],
    ["2.2.2.2", "3.3.3.3", 150],
    ["4.4.4.4", "1.1.1.1", 50],
    ["5.5.5.5", "4.4.4.4", 10],
    ["3.3.3.3", "10.10.10.10", 30],
    ["1.1.1.1", "10.10.10.10", 50],
    ["4.4.4.4", "3.3.3.3", 20]
]


def find_path_of_networks(ips, src, dst):
    import collections
    dest = collections.defaultdict(int)
    path = {}
    for i in range(len(ips)):
        dest[ips[i][0]] = float("inf")
        dest[ips[i][1]] = float("inf")
    dest[src] = 0
    # print(dest)
    for _ in range(len(dest)):
        print(dest)
        temp = dest.copy()
        for u, v, w in ips:
            if temp[v] > dest[u] + w:
                temp[v] = dest[u] + w
                if v in path and path[v]:
                    path[v].pop()
                    path[v] = u
                else:
                    path[v] = [u]
        print(temp)
        print("--------------------------")
        dest = temp.copy()

    find_path = []

    def dfs(graph, node):
        find_path.append(node)
        if node in graph:
            for other_node in graph[node]:
                dfs(graph, other_node)
    dfs(path, dst)
    print(path)
    print(dest)
    print(find_path[::-1])


# find_path_of_networks(ips, "1.1.1.1", "10.10.10.10")
find_path_of_networks(ips, "5.5.5.5", "10.10.10.10")

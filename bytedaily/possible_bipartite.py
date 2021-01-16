    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for person_a, person_b in dislikes:
            graph[person_a].add(person_b)
            graph[person_b].add(person_a)
        
        colors = {}

        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            for neighbor_node in graph[node]:
                if not dfs(neighbor_node, color ^ 1):
                    return False
            return True
        
        for node in range(1, N + 1):
            if node not in colors:
                if not dfs(node, 0):
                    return False
        return True
        # BFS    
        # colors = [-1] * (N + 1)
        # for node in range(1, N + 1):
        #     if colors[node] == -1:
        #         stk = [node]
        #         colors[node] = 0
        #         while stk:
        #             curr_node = stk.pop()
        #             for neighbor_node in graph[curr_node]:
        #                 if colors[neighbor_node] == -1:
        #                     colors[neighbor_node] = colors[curr_node] ^ 1
        #                     stk.append(neighbor_node)
        #                 elif colors[neighbor_node] == colors[curr_node]:
        #                     return False
        # return True
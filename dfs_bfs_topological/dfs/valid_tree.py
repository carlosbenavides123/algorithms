class Solution:
    def buildAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        return adjList

    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        # build an adjacency list from the edges list
        adjList = self.buildAdjacencyList(n, edges)
        visited = set()
        print(adjList)

        def hasCycle(v, parent):
            visited.add(v)
            # traverse all neighbors
            for neighbor in adjList[v]:
                if neighbor not in visited:
                    if hasCycle(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True

            return False

        # we only search with one vertex.
        # This helps to check if the graph is connected in the next step.
        if hasCycle(0, -1):
            return False

        # If the graph is connected then all vertices must be visited
        return True if len(visited) == n else False


sol = Solution()
print(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

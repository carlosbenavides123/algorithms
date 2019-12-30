# 207. Course Schedule
# Medium

# 2576

# 132

# Add to List

# Share
# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1, 0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1, 0], [0, 1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.


def canFinish(numCourses, prerequisites):
    seen = {}

    import collections
    g = collections.defaultdict(set)
    for start, end in prerequisites:
        g[start].add(end)
    print(g.keys())
    for key in g:
        print(g)
        if not dfs(g, key, seen):
            return False
    return True


def dfs(g, key, seen):
    if key in seen and seen[key] == 1:
        return True
    elif key in seen and seen[key] == 2:
        return False
    seen[key] = 2

    if key in g:
        for other_key in g[key]:
            if not dfs(g, other_key, seen):
                return False
    seen[key] = 1
    return True


print(canFinish(2, [[1, 0]]))

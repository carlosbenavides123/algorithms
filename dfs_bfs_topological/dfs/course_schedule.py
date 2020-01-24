#leetcode medium

#given a list of schedules, you have to take course one to take course two, i. e.
# [0, 1], course 0 is requires to take course 1
# given a list of a pairs, can you finish all courses
# return true if possible
def courses(arr):
    import collections
    seen = {}
    g = collections.defaultdict(set)
    for start, end in arr:
        g[start].add(end)
    for key in g:
        if not dfs(key, g, seen):
            return False
    return True

def dfs(key, g, seen):
    if key in seen and seen[key] == 2:
        return False
    if key in seen and seen[key] == 1:
        return True
    seen[key] = 2
    if key in g:
        for other_key in g[key]:
            if not dfs(other_key, g, seen):
                return False
    seen[key] = 1
    return True

print(courses([[0, 1], [1, 2], [2, 3]]))
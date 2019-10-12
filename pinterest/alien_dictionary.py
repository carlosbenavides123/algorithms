# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:

from collections import defaultdict, deque
Input = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]


def alienOrder(words):
    # a -> b
    adj = defaultdict(set)
    # in-degree
    deg = {c: 0 for w in words for c in w}
    for i, w1 in enumerate(words[:-1]):
        w2 = words[i + 1]
        for c1, c2 in zip(w1, w2):
            if c1 == c2:
                continue
            if c2 not in adj[c1]:
                deg[c2] += 1
            adj[c1].add(c2)
            break
    print("adj", adj)
    print("deg", deg)
    res = ''
    # start w 0 indegree nodes
    q = deque([c for c in deg if not deg[c]])
    while q:
        print("")
        print("start loop", q)
        c = q.popleft()
        res += c
        for n in adj[c]:
            deg[n] -= 1
            if not deg[n]:
                q.append(n)
                print("add q", q)
        print("end loop")
    return res if len(res) == len(deg) else ''


print(alienOrder(Input))
#Output: "wertf"

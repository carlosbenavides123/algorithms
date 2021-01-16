# Given a list of clothing and accessories and their  dependency relation
# (e.g. pants->underwear means you have to put on underwear first before you can put on pants).
# Decide if it's possible to properly put on everything from the list

clothes_dependencies_0 = [["pants", "underwear"], ["jacket", "sweater"], ["boots", "socks"]]
clothes_dependencies_1 = [["pants", "underwear"], ["jacket", "sweater"], ["boots", "socks"], ["socks", "boots"]]
clothes_dependencies_2 = [["pants", "underwear"], ["shorts", "underwear"], ["skirt", "underwear"], ["shirt", "body"], ["jacket", "shirt"], ["shirt", "sweater"], ["sweater", "jacket"]]

# pants -> underwear jacket->sweater boots<->socks wrong

#                                          ->  sweater
#                                          |      |
#                                          |     \/
# pants <- underwear -> shorts        jacket <- shirt <- body 
#            |
#           \/
#          skirt

import collections

# create a graph g
# g[dependency].add(dependent)
# g[underwaear].add(pants)
# create a in degree graph
# g[underwear] += 1
def can_wear_clothes(clothes):
    g = collections.defaultdict(set)
    in_deg = collections.defaultdict(int)
    all_items = set()

    for dependent, dependency in clothes:
        if dependent not in g[dependency]:
            in_deg[dependent] += 1
        g[dependency].add(dependent)
        all_items.add(dependent)
        all_items.add(dependency)

    q = collections.deque()
    for item in all_items:
        if item not in in_deg:
            q.append((item))
    # print(g)
    # print(in_deg)
    # print(q)
    res = set()
    while q:
        item = q.popleft()
        res.add(item)
        print(item)
        if item in g:
            for other_item in g[item]:
                if other_item in in_deg:
                    in_deg[other_item] -= 1
                    if in_deg[other_item] == 0:
                        q.append(other_item)
        print(q)
        print("------")
    # print(res)
    # print(all_items)
    return len(res) == len(all_items)

print(can_wear_clothes(clothes_dependencies_0))
# print(can_wear_clothes(clothes_dependencies_1))
# print(can_wear_clothes(clothes_dependencies_2))

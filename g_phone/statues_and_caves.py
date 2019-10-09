# Given array of statue heights, and an array of cave heights, find max number of statues that can fit in the cave.
# You can only insert into the cave from the opening (which is at index 0), and slide as necessary.
# For example,
# statues = [1,2,3]
# cave = [2,1,1]
# Answer: 2 because statue of height 1 can slide all the way to the back of the cave, and statue of height 2 can slide into the opening of the cave.
# Another example,
# statues = [5]
# cave = [1,20,20]
# Answer: 0 because the statue of height 5 cannot get past the opening of the cave (which is height 1).
# Statues don't have to be in same order as they were given; in fact, the interviewer recommends sorting statues first.


def statues_and_caves(statues, caves):
    res = 0
    statues.sort()

    n = len(statues)
    m = len(caves)
    statues_i = 0
    caves_j = m - 1

    while statues_i < n and caves_j >= -1:
        if statues[statues_i] <= caves[caves_j]:
            statues_i += 1
            caves_j -= 1
            res += 1
        elif statues[statues_i] > caves[caves_j]:
            caves_j -= 1
        else:
            statues_i += 1
    return res


statues = [1, 2, 3]
caves = [2, 1, 1]
print(statues_and_caves(statues, caves))

# can also do preprocessing...


def statues_and_caves(statues, caves):
    res = 0
    statues.sort()

    n = len(statues)
    m = len(caves)

    statues_i = 0
    caves_j = m - 1

    for i in range(1, m):
        caves[i] = min(caves[i-1], caves[i])

    while statues_i < n and caves_j >= -1:
        if statues[statues_i] == caves[caves_j]:
            statues_i += 1
            caves_j -= 1
            res += 1
        else:
            caves_j -= 1
    return res


statues = [1, 2, 3]
caves = [2, 1, 1]
print(statues_and_caves(statues, caves))

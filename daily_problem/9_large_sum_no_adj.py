# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# 0 0 -> take = 0 + 2, dont_take -> 0
# 0 2 -> take = 0 + 4, dont_take -> 2
# 4 8 -> take = 2 + 6, dont_take -> 4
# 8 8 -> take = no change, dont_take -> 8
# 8 13 -> take = 8 + 5, dont_take -> 8

inp = [int(x) for x in input().split(" ")]

def solve(inp):
    dont_take = take = 0
    
    for num in inp:
        temp = take
        take = max(take, dont_take + num)
        dont_take = temp
    return take
print(solve(inp))

# "5 1 1 5"
# 10
# "2 4 6 2 5"
# 13

# recursive
def solve(inp):
    if not inp:
        return 0
    return max(solve(inp[1:]), inp[0] + solve(inp[2:]))
print(solve(inp))

# dp

def solve(inp):
    cache = [0 for i in range(len(inp))]
    cache[0] = max(0, inp[0])
    cache[1] = max(cache[0], inp[1])
    
    for i in range(2, len(inp)):
        cache[i] = max(cache[i-1], cache[i-2] + inp[i])
    return cache[-1]
    
print(solve(inp))
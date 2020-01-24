# leetcode easy-med ?

# given a list of nums, return highest non adj continuous sum

# IP [4, 1, 1, 4, 2, 1]
# OP 9 (4, 4, 1)

def max_sum_no_adj(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    take = arr[0]
    no_take = 0

    for i in range(1, len(arr)):
        temp = take
        take = max(take, no_take + arr[i])
        no_take = temp
    return take

print(max_sum_no_adj([4, 1, 1, 4, 2, 1]))
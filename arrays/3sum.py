# find three numbers that equals to 0

# IP [-1,0,1,2,-1,-4]
# OP [[-1,-1,2],[-1,0,1]]

# no duplicates

def three_sum(arr):
    res = set()
    arr = sorted(arr)
    for i in range(len(arr) - 2):
        curr = arr[i]
        l = i + 1
        r = len(arr) - 1
        while l < r:
            curr_sum = curr + arr[l] + arr[r]
            if curr_sum == 0:
                res.add((curr, arr[l], arr[r]))
                l += 1
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                r -= 1
    return map(list, res)
print(three_sum([-1,0,1,2,-1,-4]))
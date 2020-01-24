# given a container array, each number represents a pillar height
# create a func that gives the largest area for water
# IP [0, 8, 3, 2, 5, 2, 8, 3, 7]
# OP 49
def container_water(arr):
    res = 0

    l = 0
    r = len(arr) - 1

    while l < r:
        res = max(res, min(arr[l], arr[r]) * (r - l) )
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return res

print(container_water([0, 8, 3, 2, 5, 2, 8, 3, 7]))
# given a array, move all even numbers to the front of the array

# [2, 3, 4, 5]
# [2, 4, 5, 3]

# explanation, two pointers
# [2, 3, 4, 5]
# [2, 5, 4, 3]
# [2, 4, 5, 3]

def move_evens(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] % 2 == 0:
            l += 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
    return arr
print(move_evens([2, 3, 4, 5]))
# [2, 4, 5, 3]
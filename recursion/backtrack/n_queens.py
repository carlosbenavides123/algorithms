def solveNQueens(n):
    res = []
    solve([-1]*n, 0, [], res)
    return res


def solve(nums, index, path, res):
    if index == len(nums):
        res.append(path)
        return
    for i in range(len(nums)):
        nums[index] = i
        if valid(nums, index):
            tmp = "."*len(nums)
            solve(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i+1:]], res)


def valid(nums, n):
    for i in range(n):
        if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
            return False
    return True


print(solveNQueens(4))


# title
# find all unique quadruplets

nums = [int(x) for x in input().split()]
target = input()

# "1 0 -1 0 -2 2"
# 0

# -2 -1 0 0 1 2 
def solve(nums, target):
    res = set()
    hmap = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            _sum = nums[i] + nums[j]
            if _sum in hmap:
                for pair in hmap[_sum]:
                    if i not in pair and j not in pair:
                        res.add(tuple(sorted([nums[i], nums[j], nums[pair[0]], nums[pair[1]]])))
            if target - _sum not in hmap:
                hmap[target - _sum] = set()
            hmap[target - _sum].add((i, j))
                        
    return map(list, res)
              
    
print(solve(nums, target))
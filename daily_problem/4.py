
# Given an array of integers, find the first missing poisitive
# integer

# example
# ip [3, 4, -1, 1]
# op 2
nums = [3, 4, -1, 1]

def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            print(v)
            nums[i], nums[v-1] = nums[v-1], nums[i]
            print(nums)
            print(nums[i], nums[v-1])
            # if nums[i] == nums[v-1]:
                # break
        print("lol")
    print(nums)
first_missing_positive(nums)
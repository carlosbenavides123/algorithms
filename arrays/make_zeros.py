class Solution:
    def moveZeros(self, nums):
        # Fill this in.
        zero_idx = 0
        for i in range(len(nums) - 2):
            if nums[i] != 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)

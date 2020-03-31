# two sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

nums = input("nums")
target = input("target")

# def sol(nums, target):
	# for i in range(len(nums)):
		# for j in range(i+1, len(nums)):
			# if target - nums[i] == nums[j]:
				# return [nums[i], nums[j]]
	# return [-1, -1]

def sol(nums, target):
	hmap = {}
	for i in range(len(nums)):
		if nums[i] in hmap:
			return [hmap[nums[i]], i]
        key = target-nums[i]
		hmap[key] = i
	return [-1, -1]
		

print(sol(nums, target))
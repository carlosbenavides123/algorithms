# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

# [5, 4, 1]
# [1, 3, 1]
# [3, 1, 3]
# [2, 43, 4]


# take 1
# take 1
# take 1
# take 2

# [20, 1, 32]
# [12, 3, 43]
# [2, 11, 3]
# [11, 21, 12]

# take 1
# take 12
# take 3
# take 11

matrix = [
	[20, 1, 3],
	[12, 3, 43],
	[2, 11, 3],
	[11, 21, 12]
]

# n*k^2 time space
def house_colors(matrix):
	cache = [[float("inf") for y in range(len(matrix[0]) + 1)] for x in range(len(matrix) + 1)]
	for i in range(len(cache[0])):
		cache[0][i] = 0
		
	for i in range(1, len(matrix) + 1):
		for j in range(1, len(matrix[0]) + 1):
			cache[i][j] = min(cache[i-1][k] for k in range(1, len(cache[0])) if k != j) + matrix[i-1][j-1]
	return cache

def house_colors(matrix):
	cache = [0 for i in range(len(matrix[0]))]
	
	for i in range(len(matrix)):
		temp_cache = []
		for j in range(len(matrix[0])):
			temp_cache.append(min(cache[k] for k in range(len(cache)) if k != j) + matrix[i][j])
		cache = temp_cache
	return cache
		
print(house_colors(matrix))
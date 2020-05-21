#This problem was asked by Snapchat.

#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

import heapq

arr = [(30, 75), (0, 50), (60, 150)]
# 0 50
# 30 75
# 60 150
# 0 50 -> 60 150
# 30 75
# need 2 rooms because 0 50 overlaps with 30 75

def sol(arr):
	heap = []
	arr.sort(key=lambda x:(x[0], x[1]))
	for item in arr:
		if not heap:
			heapq.heappush(heap, item)
		else:
			if heap[0][1] > item[0]:
				heapq.heappush(heap, item)
			else:
				heapq.heappop(heap)
				heapq.heappush(heap, item)
	print(heap)
	return len(heap)
print(sol(arr))

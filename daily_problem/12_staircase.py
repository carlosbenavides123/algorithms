#This problem was asked by Amazon.

#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
#Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

#1, 1, 1, 1
#2, 1, 1
#1, 2, 1
#1, 1, 2
#2, 2
#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number 
#from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

n = input()

# rec
def solve(n):
	if n == 0:
		return 1
	total = 0
	if n >= 1:
		total += solve(n-1)
	if n  >= 2:
		total += solve(n-2)
	return total
print(solve(n))

# bottoms up
def solve(n):
	if not n:
		return 0
	cache = [0]*(n+1)
	cache[0] = 1
	for i in range(1, n+1):
		cache[i] = cache[i-1] + cache[i-2]
	return cache[-1]
print(solve(n))

# o1 space
def solve(n):
	res = 0
	a, b = 1, 0
	for i in range(n):
		a, b = a + b, a
	return a
print(solve(n))

arr = [int(x) for x in input().split(" ")]

def solve(n, arr):
	
	cache = [0] * (n+1)
	cache[0] = 1

	for i in range(1, n+1):
		cache[i] = sum(cache[i-x] for x in arr if i - x >= 0)
	return cache[-1]
print(solve(n, arr))
	

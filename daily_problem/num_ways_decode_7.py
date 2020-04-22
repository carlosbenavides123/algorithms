#This problem was asked by Facebook.

#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

#You can assume that the messages are decodable. For example, '001' is not allowed.


# we have to realize that every option has two answers...sort of
# 11 is ak or ka
# 10 is e
# 111 - aaa or ka or ak
# a - 1
# k - 10
# num ways = 3
# what about if we have 5
# 5 - e
# 1 solution
# putting these together lets put it into 1d array

# input starts with 0, invalid
# base case empty string, res = 1
# 

string = input()

# recursive
def solve(string):
	if len(string) <= 1:
		return 1
	if string[0] == "0":
		return 0
	total = 0
	total += solve(string[1:])
	if len(string) >= 2 and int(string[:2]) <= 26:
		total += solve(string[2:])
	return total

print(solve(string))




def solve(string):
	dp = [0] * (len(string) + 1)
	dp[0] = 1
	dp[1] = 0 if string[0] == "0" else 1
	
	for i in range(2, len(string) + 1):
		print(dp, "1", i)
		if 0 <= int(string[i-1:i]) <= 10:
			dp[i] += dp[i-1]
		print(dp, "2", i)
		if 10 <= int(string[i-2:i]) <= 26:
			dp[i] += dp[i-2]
		print(dp, "3", i)
	return dp[-1]
print(solve(string))

class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        self.recurse(s, 4,  res, [])
        return ['.'.join(x) for x in res]

    def recurse(self, s, k, res, temp):
        print(temp, len(s))
        if len(s) > k*3:
            return
        if k == 0:
            res.append(temp[:])
        else:
            for i in range(min(3, len(s)-k+1)):
                print(i)
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                print(temp+[s[:i+1]], temp, k)
                self.recurse(s[i+1:], k-1, res, temp+[s[:i+1]])


sol = Solution()
print(sol.restoreIpAddresses("25525511135"))

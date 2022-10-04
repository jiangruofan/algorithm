class Solution:
    def longestAwesome(self, s: str) -> int:
        dic = {}
        dic[0] = -1
        res = 1
        x = 0
        for i, val in enumerate(s):
            x ^= 1 << int(val)
            if x not in dic:
                dic[x] = i
            else:
                res = max(res, i - dic[x])
            for j in range(10):
                if x ^ (1<<j) in dic:
                    res = max(res, i - dic[x ^ (1<<j)])
        return res

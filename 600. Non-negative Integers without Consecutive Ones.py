class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [1, 2]
        for _ in range(29):
            dp.append(dp[-1] + dp[-2])
        res = 0
        pre = -1
        for i in range(30, -1, -1):
            if (1 << i) & n:
                res += dp[i]
                if i == pre - 1:
                    break
                pre = i
            if i == 0: #这里的意思是 n这个数本身符不符合要求
                res += 1
        return res


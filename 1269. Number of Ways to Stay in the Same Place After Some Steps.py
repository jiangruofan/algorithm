class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        leng = min(arrLen, 1 + steps // 2)
        dp = [[0 for _ in range(leng)] for _ in range(steps+1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, steps+1):
            for j in range(leng):
                x = dp[i-1][j-1] if j > 0 else 0
                y = dp[i-1][j]
                z = dp[i-1][j+1] if j + 1 < leng else 0
                dp[i][j] = x + y + z
                dp[i][j] %= mod
        return dp[-1][0]

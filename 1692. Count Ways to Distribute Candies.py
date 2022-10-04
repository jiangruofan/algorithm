class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10 ** 9 +  7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] += dp[i-1][j-1] + (dp[i-1][j] * j) % mod
                dp[i][j] %= mod
        return dp[-1][-1]
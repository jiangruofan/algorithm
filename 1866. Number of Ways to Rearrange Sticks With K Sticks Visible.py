class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[1][1] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * (i-1)
                dp[i][j] %= mod
        return dp[-1][-1] % mod
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        # dp[i][j] = dp[i-1][j - (i-1-k)] (for k in range(i))
        # dp[i][j-1] = dp[i-1][j-1 - (i-1-k)] (for k in range(i))
        # dp[i][j] = dp[i][j-1] - dp[i-1][j-i] + dp[i-1][j]
        dp = [0 for _ in range(k+1)]
        dp[0] = 1
        for i in range(1, n+1):
            dp1 = [0 for _ in range(k+1)]
            dp1[0] = 1
            for j in range(1, k+1):
                dp1[j] = dp1[j-1] - (dp[j-i] if j-i >= 0 else 0) + dp[j]
            dp = dp1
        return dp[-1] % (10 ** 9 + 7)
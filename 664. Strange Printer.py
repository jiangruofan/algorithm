class Solution:
    def strangePrinter(self, s: str) -> int:
        leng = len(s)
        dp = [[0] * leng for _ in range(leng)]
        for i in range(leng):
            dp[i][i] = 1
        for i in range(leng-1, -1, -1):
            for j in range(i+1, leng):
                if s[j] == s[i]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j))
        return dp[0][-1]
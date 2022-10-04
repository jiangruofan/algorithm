class Solution:
    def minInsertions(self, s: str) -> int:
        s = list(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for leng in range(2, n+1):
            for i in range(n-leng+1):
                j = i + leng - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if i + 1 < j else 0
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][-1]
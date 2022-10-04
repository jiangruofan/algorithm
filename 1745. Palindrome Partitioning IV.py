class Solution:
    def checkPartitioning(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j + 1][i - 1] if i - j > 1 else True

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if dp[0][i] and dp[i + 1][j] and dp[j + 1][-1]:
                    return True

        return False
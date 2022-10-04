class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if n == 1:
            return 1
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, k + 1):
            dp[1][i] = 1
        res = -1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = 1 + dp[i - 1][j] + dp[i - 1][j - 1]
            if dp[i][k] >= n:
                res = i
                break
        return res




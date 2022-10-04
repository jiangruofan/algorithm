class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for x, y, k in prices:
            dp[x][y] = k
        for i in range(1, m+1):
            for j in range(1, n+1):
                for x in range(1, i // 2 + 1):
                    dp[i][j] = max(dp[i][j], dp[x][j] + dp[i-x][j])
                for y in range(1, j // 2 + 1):
                    dp[i][j] = max(dp[i][j], dp[i][y] + dp[i][j-y])
        return dp[-1][-1]

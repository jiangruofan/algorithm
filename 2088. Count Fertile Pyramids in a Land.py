class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == 0:
                    dp[i][j] = -1
                else:
                    a = dp[i + 1][j - 1] if i + 1 < m and j - 1 >= 0 else -1
                    b = dp[i + 1][j] if i + 1 < m else -1
                    c = dp[i + 1][j + 1] if i + 1 < m and j + 1 < n else -1
                    dp[i][j] = min(a, b, c) + 1
                    res += dp[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dp[i][j] = -1
                else:
                    a = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else -1
                    b = dp[i - 1][j] if i - 1 >= 0 else -1
                    c = dp[i - 1][j + 1] if i - 1 >= 0 and j + 1 < n else -1
                    dp[i][j] = min(a, b, c) + 1
                    res += dp[i][j]

        return res
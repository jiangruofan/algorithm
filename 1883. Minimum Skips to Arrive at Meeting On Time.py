class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        dist = [-1] + dist
        n = len(dist)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            dp[i][0] = ceil(dp[i - 1][0] + dist[i] / speed - 1e-8)
            for j in range(1, i + 1):
                x = dp[i - 1][j - 1] + dist[i] / speed
                y = ceil(dp[i - 1][j] + dist[i] / speed - 1e-8) if dp[i - 1][j] != float('inf') else float('inf')
                dp[i][j] = min(x, y)

        for i in range(n):
            if dp[-1][i] <= hoursBefore:
                return i

        return -1
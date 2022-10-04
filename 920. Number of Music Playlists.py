class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(n+1)] for _ in range(goal+1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                dp[i][j] += dp[i-1][j-1] * (n-j+1)
                dp[i][j] %= mod
                dp[i][j] += dp[i-1][j] * max(0, j-k)
                dp[i][j] %= mod
        return dp[-1][-1]
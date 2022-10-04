class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n)]
        for i in range(1, m + 1):
            dp[0][i][1] = 1
        mod = 10 ** 9 + 7
        for i in range(1, n):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    for x in range(1, j):
                        dp[i][j][p] += dp[i - 1][x][p - 1]
                    dp[i][j][p] += dp[i - 1][j][p] * j
        return sum(dp[-1][i][-1] for i in range(1, m + 1)) % mod


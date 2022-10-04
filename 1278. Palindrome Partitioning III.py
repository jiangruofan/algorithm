class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        s = list(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                l, r = j, i
                while l < r:
                    if s[l] != s[r]:
                        dp[j][i] += 1
                    l += 1
                    r -= 1

        dp1 = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if j == 1:
                    dp1[i][j] = dp[0][i]
                    continue
                for h in range(i):
                    dp1[i][j] = min(dp1[i][j], dp1[h][j - 1] + dp[h + 1][i])

        return dp1[-1][-1]
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        cnt = {0: "a", 1: "b", 2: "c", 3: "d"}
        next1 = [[float('inf') for _ in range(4)] for _ in range(n)]
        pre = [[-float('inf') for _ in range(4)] for _ in range(n)]

        for k in range(4):
            l = 0
            for r in range(n):
                if s[r] == cnt[k]:
                    while l <= r:
                        next1[l][k] = r
                        l += 1

        for k in range(4):
            r = n - 1
            for l in range(n - 1, -1, -1):
                if s[l] == cnt[k]:
                    while l <= r:
                        pre[r][k] = l
                        r -= 1

        for leng in range(n):
            for i in range(n - leng):
                j = i + leng
                for k in range(4):
                    if next1[i][k] < pre[j][k]:
                        dp[i][j] += dp[next1[i][k] + 1][pre[j][k] - 1] + 1
                        dp[i][j] %= mod
                    if next1[i][k] <= pre[j][k]:
                        dp[i][j] += 1
        return dp[0][-1] % mod
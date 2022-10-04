class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        total = []

        def dfs(path):
            if len(path) == m:
                total.append(tuple(path[::]))
                return
            for i in range(3):
                if path and path[-1] == i:
                    continue
                path.append(i)
                dfs(path)
                path.pop()

        dfs([])

        @cache
        def check(x, y):
            for i in range(m):
                if x[i] == y[i]:
                    return False
            return True

        dp = [[0 for _ in range(len(total))] for _ in range(n)]
        for i in range(len(total)):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(len(total)):
                for k in range(len(total)):
                    if check(total[j], total[k]):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod

        return sum(dp[-1]) % mod

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        presum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                presum[i][j] += 1 if pizza[i][j] == "A" else 0
                presum[i][j] += presum[i + 1][j] if i + 1 < m else 0
                presum[i][j] += presum[i][j + 1] if j + 1 < n else 0
                presum[i][j] -= presum[i + 1][j + 1] if i + 1 < m and j + 1 < n else 0

        @cache
        def dfs(x, y, num):
            if presum[x][y] < num:
                return 0
            if num == 1:
                return 1
            res = 0
            for i in range(x + 1, m):
                if presum[x][y] - presum[i][y] > 0:
                    res += dfs(i, y, num - 1)
                    res %= mod
            for i in range(y + 1, n):
                if presum[x][y] - presum[x][i] > 0:
                    res += dfs(x, i, num - 1)
                    res %= mod
            return res

        return dfs(0, 0, k)
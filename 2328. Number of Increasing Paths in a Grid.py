class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        def transform(x, y):
            return x * n + y

        def transform1(node):
            return (node // n, node % n)

        @cache
        def dfs(node):
            res = 1
            x, y = transform1(node)
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[x][y]:
                    res += dfs(transform(i, j))
                    res %= mod
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(transform(i, j))
                ans %= mod
        return ans


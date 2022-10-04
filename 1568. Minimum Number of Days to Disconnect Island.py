class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = -1
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    dfs(i, j)

        def count():
            num = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        num += 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == -1:
                        grid[i][j] = 1
            return num

        if count() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
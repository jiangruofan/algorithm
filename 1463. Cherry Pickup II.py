class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, x1, y1):
            total = grid[x][y] + grid[x1][y1] if y != y1 else grid[x][y]
            if x == m - 1:
                return total
            res = 0
            for i in (y - 1, y, y + 1):
                for j in (y1 - 1, y1, y1 + 1):
                    if 0 <= i < n and 0 <= j < n:
                        res = max(res, dfs(x + 1, i, x1 + 1, j))
            return res + total

        return dfs(0, 0, 0, n - 1)

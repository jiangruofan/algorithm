class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, total):
            if total < 0:
                return False
            if x == m - 1 and y == n - 1:
                if total == 0:
                    return True
                else:
                    return False
            for i, j in ((x + 1, y), (x, y + 1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == "(" and dfs(i, j, total + 1):
                        return True
                    if grid[i][j] == ")" and dfs(i, j, total - 1):
                        return True
            return False

        if grid[0][0] == ")":
            return False
        else:
            return dfs(0, 0, 1)


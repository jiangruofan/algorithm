class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = 0
            seen.add((x, y))
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    dfs(i, j)

        def cal(seen):
            res = 0
            seen = list(seen)
            for i, (x, y) in enumerate(seen):
                for j in range(i + 1, len(seen)):
                    get = (x - seen[j][0]) ** 2 + (y - seen[j][1]) ** 2
                    res += sqrt(get)
            return res

        total = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                seen = set()
                dfs(i, j)
                get = cal(seen)
                if not total:
                    total.add(get)
                    continue
                judge = True
                for val in total:
                    if abs(get - val) < 1e-5:
                        judge = False
                        break
                if judge:
                    total.add(get)

        return len(total)
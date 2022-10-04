class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        fa = [i for i in range(m * n)]
        size = [1 for _ in range(m * n)]
        res = []

        def find(x):
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 < fa2:
                fa[fa2] = fa1
                size[fa1] += size[fa2]
            elif fa2 < fa1:
                fa[fa1] = fa2
                size[fa2] += size[fa1]

        grid_1 = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i, j in hits:
            grid[i][j] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        union(x * n + y, i * n + j)

        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]
            if grid_1[x][y] == 0:
                res.append(0)
                continue
            grid[x][y] = 1
            judge = True if x == 0 else False
            cnt = 0
            for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                    if find(x * n + y) == find(x1 * n + y1):
                        continue
                    if find(x1 * n + y1) < n:
                        judge = True
                    else:
                        cnt += size[find(x1 * n + y1)]
                    union(x * n + y, x1 * n + y1)
            res.append(cnt if judge else 0)

        return res[::-1]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        sign = 2
        n = len(grid)
        cnt = Counter()
        def dfs(x, y):
            nonlocal total
            total += 1
            grid[x][y] = sign
            for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n and grid[x1][y1] == 1:
                    dfs(x1, y1)
        for i in range(n):
            for j in range(n):
                total = 0
                if grid[i][j] == 1:
                    dfs(i, j)
                    cnt[sign] = total
                    sign += 1
        res = max(cnt.values()) if cnt.values() else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    count = 1
                    seen = set()
                    for i1, j1 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < n and grid[i1][j1] not in seen:
                            seen.add(grid[i1][j1])
                            count += cnt[grid[i1][j1]]
                    res = max(res, count)
        return res

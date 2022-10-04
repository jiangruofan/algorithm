class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        dic = defaultdict(list)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        dic[i * n + j].append(x * n + y)

        match = defaultdict(lambda: -1)

        def find(x):
            for val in dic[x]:
                if visited[val]:
                    continue
                visited[val] = True
                if match[val] == -1 or find(match[val]):
                    match[x] = val
                    match[val] = x
                    return True
            return False

        cnt = 0
        for i in range(m * n):
            if match[i] != -1:
                continue
            visited = defaultdict(lambda: False)
            if find(i):
                cnt += 1
        return cnt
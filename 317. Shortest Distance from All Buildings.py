class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = [[0] * n for _ in range(m)]
        deq = deque()
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    deq.append((i, j, k))
                    k += 1
        leng = len(deq)
        visited = [[[0] * leng for _ in range(n)] for _ in range(m)]
        k = 1
        res = float('inf')
        while deq:
            leng1 = len(deq)
            for _ in range(leng1):
                x, y, z = deq.popleft()
                for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != 1 and grid[i][j] != 2 and visited[i][j][z] != 1:
                        grid[i][j] -= k
                        visited[i][j][z] = 1
                        count[i][j] += 1
                        if count[i][j] == leng:
                            res = min(res, -grid[i][j])
                        deq.append((i, j, z))
            k += 1
        return -1 if res == float('inf') else res


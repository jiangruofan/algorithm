class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deq = deque([(0, 0, 0)])
        seen = set([(0, 0)])
        while deq:
            x, y, num = deq.popleft()
            if x == m - 1 and y == n - 1:
                return num
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen:
                    if grid[i][j] == 1:
                        deq.append((i, j, num + 1))
                    else:
                        deq.appendleft((i, j, num))
                    seen.add((i, j))
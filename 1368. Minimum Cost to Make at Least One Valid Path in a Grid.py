class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deq = deque([(0, 0, 0)])
        seen = set()
        dic = {1:(0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}

        while deq:
            cost, x, y = deq.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            if x * n + y in seen:
                continue
            seen.add(x * n + y)

            for i in range(1, 5):
                x1, y1 = x + dic[i][0], y + dic[i][1]
                if 0 <= x1 < m and 0 <= y1 < n and x1 * n + y1 not in seen:
                    if grid[x][y] == i:
                        deq.appendleft((cost, x1, y1))
                    else:
                        deq.append((cost + 1, x1, y1))
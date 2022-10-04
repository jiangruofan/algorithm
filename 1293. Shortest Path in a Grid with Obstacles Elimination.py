class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        deq = deque([(0, 0, k)])
        set1 = set([(0, 0, k)])
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x, y, left = deq.popleft()
                if x == m - 1 and y == n - 1:
                    return cnt
                for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if x1 >= 0 and y1 >= 0 and x1 < m and y1 < n:
                        if grid[x1][y1] == 1 and left != 0 and (x1, y1, left - 1) not in set1:
                            deq.append((x1, y1, left - 1))
                            set1.add((x1, y1, left - 1))
                        elif grid[x1][y1] == 0 and (x1, y1, left) not in set1:
                            deq.append((x1, y1, left))
                            set1.add((x1, y1, left))
            cnt += 1
        return -1

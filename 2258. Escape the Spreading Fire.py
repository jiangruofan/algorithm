class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(time):
            fires = set()
            fires1 = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fires.add((i, j))
                        fires1.add((i, j))

            def spread():
                nonlocal fires1
                new = set()
                for x, y in fires1:
                    for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] != 2 and (x1, y1) not in fires:
                            fires.add((x1, y1))
                            new.add((x1, y1))
                fires1 = new

            for _ in range(time):
                spread()

            deq = deque([(0, 0)])
            seen = set([(0, 0)])
            while deq:
                leng = len(deq)
                for _ in range(leng):
                    x, y = deq.popleft()
                    if (x, y) in fires:
                        continue
                    for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= i < m and 0 <= j < n and (i, j) not in fires and (i, j) not in seen and grid[i][j] != 2:
                            if i == m - 1 and j == n - 1:
                                return True
                            deq.append((i, j))
                            seen.add((i, j))
                spread()

            return False

        if not check(0):
            return -1

        l, r = 0, m * n
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l if l != m * n else 10 ** 9

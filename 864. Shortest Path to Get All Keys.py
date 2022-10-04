class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            grid[i] = list(grid[i])
            for j in range(n):
                if grid[i][j] == "@":
                    startx = i
                    starty = j
                if grid[i][j].islower():
                    cnt += 1

        deq = deque([(startx, starty, 0)])
        seen = set([(startx, starty, 0)])
        res = 0
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x, y, keys = deq.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != "#":
                        if grid[i][j] == "." or grid[i][j] == "@":
                            if (i, j, keys) not in seen:
                                deq.append((i, j, keys))
                                seen.add((i, j, keys))
                        elif grid[i][j].islower():
                            keys1 = keys | (1 << (ord(grid[i][j]) - ord("a")))
                            cnt1 = 0
                            for i1 in range(8):
                                if keys1 & (1 << i1):
                                    cnt1 += 1
                            if cnt1 == cnt:
                                return res + 1

                            if (i, j, keys1) not in seen:
                                deq.append((i, j, keys1))
                                seen.add((i, j, keys1))
                        else:
                            if keys & (1 << (ord(grid[i][j]) - ord("A"))) and (i, j, keys) not in seen:
                                deq.append((i, j, keys))
                                seen.add((i, j, keys))
            res += 1

        return -1


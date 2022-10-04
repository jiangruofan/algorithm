class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deq = deque([(0, 1, "h")])
        seen = set(deq)
        res = 0
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x, y, dir1 = deq.popleft()
                if x == m - 1 and y == n - 1 and dir1 =="h":
                    return res
                if dir1 == "h":
                    if y + 1 < n and grid[x][y+1] == 0 and (x, y+1, "h") not in seen:
                        deq.append(((x, y+1, "h")))
                        seen.add((x, y+1, "h"))
                    if x + 1 < m and grid[x+1][y] == 0 and grid[x+1][y-1] == 0:
                        if (x+1, y, "h") not in seen:
                            deq.append((x+1, y, "h"))
                            seen.add((x+1, y, "h"))
                        if (x+1, y-1, "v") not in seen:
                            deq.append((x+1, y-1, "v"))
                            seen.add((x+1, y-1, "v"))
                else:
                    if y + 1 < n and grid[x][y+1] == 0 and grid[x-1][y+1] == 0:
                        if (x, y+1, "v") not in seen:
                            deq.append((x, y+1, "v"))
                            seen.add((x, y+1, "v"))
                        if (x-1, y+1, "h") not in seen:
                            deq.append((x-1, y+1, "h"))
                            seen.add((x-1, y+1, "h"))
                    if x + 1 < m and grid[x+1][y] == 0 and (x+1, y, "v") not in seen:
                        deq.append((x+1, y, "v"))
                        seen.add((x+1, y, "v"))
            res += 1
        return -1

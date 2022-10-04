class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "T":
                    target_x = i
                    target_y = j
                    grid[i][j] = "."
                if grid[i][j] == "B":
                    box_x = i
                    box_y = j
                    grid[i][j] = "."
                if grid[i][j] == "S":
                    player_x = i
                    player_y = j
                    grid[i][j] = "."
        deq = deque([(box_x, box_y, player_x, player_y, 0)])
        seen = set([(box_x, box_y, player_x, player_y)])


        while deq:
            bx, by, px, py, times = deq.popleft()
            if bx == target_x and by == target_y:
                return times

            for i, j in ((px+1, py), (px-1, py), (px, py+1), (px, py-1)):
                if 0 <= i < m and 0 <= j < n and (i != bx or j != by) and grid[i][j] == "." and (bx, by, i, j) not in seen:
                    deq.appendleft((bx, by, i, j, times))
                    seen.add((bx, by, i, j))

            if abs(bx-px) + abs(by-py) == 1:
                for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if px + i == bx and py + j == by and 0 <= bx + i < m and 0 <= by + j < n and grid[bx+i][by+j] == "." and (bx+i, by+j, bx, by) not in seen:
                        deq.append((bx+i, by+j, bx, by, times+1))
                        seen.add((bx+i, by+j, bx, by))

        return -1
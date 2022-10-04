class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        status = [[[[[0] * 3 for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "F":
                    x_food, y_food = i, j
                if grid[i][j] == "C":
                    cat_x, cat_y = i, j
                if grid[i][j] == "M":
                    mouse_x, mouse_y = i, j
        deq = deque()
        for i in range(m):
            for j in range(n):
                if i == x_food and j == y_food:
                    continue
                if grid[i][j] == "#":
                    continue
                status[i][j][x_food][y_food][1] = 2
                status[x_food][y_food][i][j][2] = 1
                deq.append((i, j, x_food, y_food, 1))
                deq.append((x_food, y_food, i, j, 2))
                status[i][j][i][j][1] = 2
                status[i][j][i][j][2] = 2
                deq.append((i, j, i, j, 1))
                deq.append((i, j, i, j, 2))

        def findParent(x1, y1, x2, y2, t):
            res = []
            if t == 1:
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    for num in range(catJump+1):
                        x, y = x2 + i * num, y2 + j * num
                        if x < 0 or y < 0 or x >= m or y >= n:
                            break
                        if grid[x][y] == "#":
                            break
                        res.append((x1, y1, x, y, 2))
            else:
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    for num in range(mouseJump+1):
                        x, y = x1 + i * num, y1 + j * num
                        if x < 0 or y < 0 or x >= m or y >= n:
                            break
                        if grid[x][y] == "#":
                            break
                        res.append((x, y, x2, y2, 1))
            return res

        def judgeParent(x1, y1, x2, y2, t):
            if t == 1:
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    for num in range(mouseJump+1):
                        x, y = x1 + i * num, y1 + j * num
                        if x < 0 or y < 0 or x >= m or y >= n:
                            break
                        if grid[x][y] == "#":
                            break
                        if status[x][y][x2][y2][2] != 2:
                            return False
            else:
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    for num in range(catJump+1):
                        x, y = x2 + i * num, y2 + j * num
                        if x < 0 or y < 0 or x >= m or y >= n:
                            break
                        if grid[x][y] == "#":
                            break
                        if status[x1][y1][x][y][1] != 1:
                            return False
            return True

        cnt = 0
        while deq:
            cnt += 1
            if cnt > 2000:
                return False
            leng = len(deq)
            for _ in range(leng):
                x_m, y_m, x_c, y_c, t = deq.popleft()
                cur_status = status[x_m][y_m][x_c][y_c][t]
                for val in findParent(x_m, y_m, x_c, y_c, t):
                    if status[val[0]][val[1]][val[2]][val[3]][val[4]] != 0:
                        continue
                    if t + cur_status == 3 or judgeParent(val[0], val[1], val[2], val[3], val[4]):
                        status[val[0]][val[1]][val[2]][val[3]][val[4]] = cur_status
                        deq.append((val[0], val[1], val[2], val[3], val[4]))
        return status[mouse_x][mouse_y][cat_x][cat_y][1] == 1
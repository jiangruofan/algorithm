class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        res = m * n
        seen = [[0 for _ in range(n)] for _ in range(m)]

        def getStart():
            for i in range(m):
                for j in range(n):
                    if seen[i][j] == 0:
                        return (i, j)

        def check(x, y, size):
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if seen[i][j] == 1:
                        return False
            return True

        def cover(x, y, size, val):
            for i in range(x, x + size):
                for j in range(y, y + size):
                    seen[i][j] = val

        def cal(cnt, total):
            nonlocal res
            if cnt >= res:
                return
            if total == m * n:
                res = min(res, cnt)
                return
            x, y = getStart()
            for size in range(min(m - x, n - y), 0, -1):
                if check(x, y, size):
                    cover(x, y, size, 1)
                    cal(cnt + 1, total + size ** 2)
                    cover(x, y, size, 0)

        cal(0, 0)

        return res
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        mod = pow(3, n - 1)

        @cache
        def dfs(x, y, inleft, outleft, status):
            if y == n:
                return dfs(x + 1, 0, inleft, outleft, status)
            if x == m:
                return 0

            up = status // mod
            left = status % 3

            change = status % mod
            change *= 3

            res = dfs(x, y + 1, inleft, outleft, change)
            if inleft:
                add1 = 120
                if up == 1:
                    add1 -= 60
                elif up == 2:
                    add1 -= 10
                if y:
                    if left == 1:
                        add1 -= 60
                    elif left == 2:
                        add1 -= 10
                res = max(res, add1 + dfs(x, y + 1, inleft - 1, outleft, change + 1))

            if outleft:
                add1 = 40
                if up == 1:
                    add1 -= 10
                elif up == 2:
                    add1 += 40
                if y:
                    if left == 1:
                        add1 -= 10
                    elif left == 2:
                        add1 += 40
                res = max(res, add1 + dfs(x, y + 1, inleft, outleft - 1, change + 2))

            return res

        return dfs(0, 0, introvertsCount, extrovertsCount, 0)


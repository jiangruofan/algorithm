# 0 represents no person 1 represents there is a person 2 represents block
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        mod = pow(3, n)
        mod1 = mod // 3
        mod2 = mod1 // 3

        @cache
        def dfs(x, y, status):
            if y == n:
                return dfs(x + 1, 0, status)
            if x == m:
                return 0

            topleft = status // mod if y != 0 else 0
            left = status % 3 if y != 0 else 0
            topright = status % mod % mod1 // mod2 if y != n - 1 else 0

            change = status % mod
            change *= 3

            if seats[x][y] == "#":
                return dfs(x, y + 1, change + 2)

            res = dfs(x, y + 1, change)

            if topleft != 1 and left != 1 and topright != 1:
                res = max(res, 1 + dfs(x, y + 1, change + 1))

            return res

        return dfs(0, 0, 0)

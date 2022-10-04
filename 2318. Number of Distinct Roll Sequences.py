class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6

        mod = 10 ** 9 + 7

        dp = [[0 for _ in range(7)] for _ in range(7)]

        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and gcd(i, j) == 1:
                    dp[i][j] += 1

        for i in range(3, n + 1):
            new = [[0 for _ in range(7)] for _ in range(7)]
            for x in range(1, 7):
                for y in range(1, 7):
                    if x == y or gcd(x, y) != 1:
                        continue
                    for z in range(1, 7):
                        if x == z:
                            continue
                        new[x][y] += dp[y][z]
                        new[x][y] %= mod
            dp = new

        res = 0
        for i in range(1, 7):
            for j in range(1, 7):
                res += dp[i][j]
                res %= mod
        return res
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        total = []

        def dfs(path):
            if len(path) == 3:
                total.append(path[::])
                return
            for i in range(3):
                if path and path[-1] == i:
                    continue
                path.append(i)
                dfs(path)
                path.pop()

        dfs([])

        def check(x, y):
            for i in range(3):
                if x[i] == y[i]:
                    return False
            return True

        dp = [1 for _ in range(len(total))]
        for i in range(2, n + 1):
            new = [0 for _ in range(len(total))]
            for j in range(len(total)):
                for k in range(len(total)):
                    if check(total[j], total[k]):
                        new[j] += dp[k]
                        new[j] %= mod
            dp = new
        return sum(dp) % mod

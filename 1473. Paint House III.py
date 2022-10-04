class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf') for _ in range(n + 1)] for _ in range(target + 1)] for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][0][i] = 0

        for i in range(1, m + 1):
            if houses[i - 1] != 0:
                k = houses[i - 1]
                for j in range(1, target + 1):
                    for h in range(1, n + 1):
                        if k == h:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][h])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][h])
            else:
                for j in range(1, target + 1):
                    list1 = [(dp[i - 1][j - 1][j1], j1) for j1 in range(1, n + 1)]
                    list1.sort()
                    for h in range(1, n + 1):
                        dp[i][j][h] = dp[i - 1][j][h]
                        dp[i][j][h] = min(dp[i][j][h], list1[0][0] if list1[0][1] != h else list1[1][0])
                        dp[i][j][h] += cost[i - 1][h - 1]

        res = float('inf')
        for i in range(1, n + 1):
            res = min(res, dp[-1][-1][i])
        return res if res != float('inf') else -1
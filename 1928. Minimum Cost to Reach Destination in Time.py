class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        dp = [[float('inf') for _ in range(n)] for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]

        for i in range(1, maxTime + 1):
            for x, y, time in edges:
                if time > i:
                    continue
                dp[i][x] = min(dp[i][x], dp[i - time][y] + passingFees[x])
                dp[i][y] = min(dp[i][y], dp[i - time][x] + passingFees[y])

        res = min(dp[i][-1] for i in range(maxTime + 1))
        return res if res != float('inf') else -1
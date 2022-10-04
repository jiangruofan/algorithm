class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for i in range(1, n):
            min1 = float('inf')
            sign = -1
            for j in range(k):
                if dp[i - 1][j] < min1:
                    min1 = dp[i - 1][j]
                    sign = j
            for j in range(k):
                if j != sign:
                    dp[i][j] = min1
                else:
                    for h in range(k):
                        if h != j:
                            dp[i][j] = min(dp[i][j], dp[i - 1][h])
                dp[i][j] += costs[i][j]

        return min(dp[-1])
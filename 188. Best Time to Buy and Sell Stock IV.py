class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        dp = [[0] * 2 * k for _ in range(len(prices))]
        for i in range(0, 2 * k, 2):
            dp[0][i] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            for j in range(2, 2 * k, 2):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
            for h in range(1, 2 * k, 2):
                dp[i][h] = max(dp[i-1][h], dp[i-1][h-1] + prices[i])
        return max(dp[-1])
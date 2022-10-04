class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        n = len(cuts)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for leng in range(2, n + 1):
            for i in range(n - leng + 1):
                j = i + leng - 1
                if leng == 2:
                    dp[i][j] = 0
                    continue
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])

        return dp[0][-1]

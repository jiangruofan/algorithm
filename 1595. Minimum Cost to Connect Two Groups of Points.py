class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        dp = [[1300 for _ in range(1 << n)] for _ in range(m + 1)]

        dp[0][0] = 0

        @cache
        def cal(i, subset):
            res = 0
            index = 0
            while subset:
                if subset & 1:
                    res += cost[i][index]
                subset >>= 1
                index += 1
            return res

        @cache
        def cal2(i, j):
            res = 1300
            index = 0
            while j:
                if j & 1:
                    res = min(res, cost[i][index])
                j >>= 1
                index += 1
            return res

        for i in range(1, m + 1):
            for j in range(1, 1 << n):
                subset = j
                while subset > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - subset] + cal(i - 1, subset))
                    subset = (subset - 1) & j
                min1 = cal2(i - 1, j)
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + min1)

        return dp[-1][-1]
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        dp = Counter()
        dp[0] = 0
        for i in range(n // 2):
            val = rods[i]
            for key, val1 in list(dp.items()):
                dp[key + val] = max(dp[key + val], val1 + val)
                dp[key - val] = max(dp[key - val], val1)

        dp1 = Counter()
        dp1[0] = 0
        for i in range(n // 2, n):
            val = rods[i]
            for key, val1 in list(dp1.items()):
                dp1[key + val] = max(dp1[key + val], val1 + val)
                dp1[key - val] = max(dp1[key - val], val1)

        res = 0
        for key, val in dp.items():
            if dp1[-key] == 0:
                continue
            res = max(res, val + dp1[-key])

        return res

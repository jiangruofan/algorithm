class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        res = 0
        for list1 in cuboids:
            list1.sort()
        cuboids.sort(reverse=True)
        n = len(cuboids)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[i][0] <= cuboids[j][0] and cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
            res = max(res, dp[i])
        return res
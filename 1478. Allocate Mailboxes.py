class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dis = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                sum1 = 0
                for h in range(i, j+1):
                    sum1 += abs(houses[h] - houses[(i+j)//2])
                dis[i][j] = sum1

        dp = [[float('inf') for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = dis[0][i]
        for i in range(n):
            for j in range(2, k+1):
                for h in range(1, i+1):
                    dp[i][j] = min(dp[i][j], dp[h-1][j-1] + dis[h][i])
        return dp[-1][-1]
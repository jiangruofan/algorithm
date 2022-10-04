class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        leng = len(startTime)
        order = [i for i in range(leng)]
        order.sort(key = lambda x : endTime[x])
        endTime.sort()
        dp = [0] * leng
        dp[0] = profit[order[0]]
        for i in range(1, leng):
            x = bisect_right(endTime, startTime[order[i]]) - 1
            dp[i] = max(dp[i-1], dp[x] + profit[order[i]])
        return dp[-1]
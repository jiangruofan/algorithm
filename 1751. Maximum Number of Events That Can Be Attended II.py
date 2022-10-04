class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x : x[1])
        list1 = [val[1] for val in events]
        dp = [[0 for _ in range(k+1)] for _ in range(len(events))]
        res = 0
        dp[0][1] = events[0][2]
        for i in range(1, len(events)):
            dp[i][1] = max(dp[i-1][1], events[i][2])
            for j in range(2, k+1):
                index = bisect_left(list1, events[i][0])
                if index == 0:
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = max(dp[i-1][j], events[i][2] + dp[index-1][j-1])
        return max(dp[-1])


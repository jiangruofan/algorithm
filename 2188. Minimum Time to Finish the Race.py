class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        leng = len(tires)
        pre = [float('inf') for _ in range(18)]
        for val in tires:
            count = val[0]
            sum1 = val[0]
            for i in range(1, 18):
                pre[i] = min(pre[i], sum1)
                count = count * val[1]
                sum1 += count

        dp = [float('inf') for _ in range(numLaps + 1)]
        dp[0] = 0
        for i in range(1, numLaps + 1):
            for j in range(max(0, i - 17), i):
                dp[i] = min(dp[i], pre[i - j] + dp[j] + changeTime)
        return dp[-1] - changeTime
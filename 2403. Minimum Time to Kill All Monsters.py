class Solution:
    def minimumTime(self, power: List[int]) -> int:
        leng = len(power)
        dp = [float('inf') for _ in range(1<<leng)]
        dp[0] = 0
        for i in range(1, 1 << leng):
            gain = i.bit_count()
            for j in range(leng):
                if i & (1 << j):
                    dp[i] = min(dp[i], dp[i & (~(1<<j))] + ceil(power[j] / gain))
        return dp[-1]
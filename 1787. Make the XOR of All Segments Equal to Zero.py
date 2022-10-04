class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        cnt = [Counter() for _ in range(k)]
        leng = len(nums)
        for i in range(leng):
            cnt[i%k][nums[i]] += 1
        dp = [[float('inf') for _ in range(1<<10)] for _ in range(k+1)]
        dp[0][0] = 0
        for i in range(1, k+1):
            pre = min(dp[i-1])
            for j in range(1<<10):
                total = leng // k + (1 if i <= leng % k else 0)
                for key in cnt[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j^key] + total - cnt[i-1][key])
                dp[i][j] = min(dp[i][j], total + pre)
        return dp[-1][0]

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        leng1, leng2 = len(nums1), len(nums2)
        dp = [[-float('inf') for _ in range(leng2)] for _ in range(leng1)]
        for i in range(leng1):
            for j in range(leng2):
                x = dp[i-1][j] if i > 0 else -float('inf')
                y = dp[i][j-1] if j > 0 else -float('inf')
                z = max((dp[i-1][j-1] if i > 0 and j > 0 else 0), 0) + nums1[i] * nums2[j]
                dp[i][j] = max(dp[i][j], x, y, z)
        return dp[-1][-1]
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        leng = len(nums1)
        dp = [float('inf') for _ in range(1<<leng)]
        dp[0] = 0
        for state in range(1, 1<<leng):
            for i in range(leng):
                if state & (1 << i):
                    dp[state] = min(dp[state], dp[state ^ (1 << i)] + (nums1[i] ^ nums2[state.bit_count()-1]))
        return dp[-1]

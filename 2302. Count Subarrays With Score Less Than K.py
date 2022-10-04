class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum1 = 0
        l = 0
        res = 0
        for i, val in enumerate(nums):
            sum1 += val
            while sum1 * (i - l + 1) >= k:
                sum1 -= nums[l]
                l += 1
            res += i - l + 1
        return res

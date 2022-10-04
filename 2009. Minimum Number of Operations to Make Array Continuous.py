class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = len(nums)
        nums = sorted(set(nums))
        r = 0
        res = float('inf')
        for i in range(len(nums)):
            while r < len(nums) and nums[r] <= nums[i] + total - 1:
                r += 1
            res = min(res, total - r + i)
        return res
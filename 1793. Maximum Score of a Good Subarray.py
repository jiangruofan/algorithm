class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        res = 0
        min1 = nums[k]
        while l >= 0 or r < len(nums):
            while l >= 0 and nums[l] >= min1:
                l -= 1
            while r < len(nums) and nums[r] >= min1:
                r += 1
            res = max(res, (r - l - 1) * min1)
            min1 = max(nums[l] if l >= 0 else -float('inf'), nums[r] if r < len(nums) else -float('inf'))

        return res
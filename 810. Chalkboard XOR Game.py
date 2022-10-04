class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True

        res = 0
        for val in nums:
            res ^= val
        return res == 0
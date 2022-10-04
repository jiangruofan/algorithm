class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = float('inf')
        for val in nums:
            if val <= 0:
                continue
            elif val == 1:
                cur = 2
                while cur in nums:
                    cur += 1
                return cur
        return 1
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        cur = float('inf')
        for i in range(len(nums)-1 ,-1, -1):
            if nums[i] <= cur:
                cur = nums[i]
                continue
            x = ceil(nums[i]/cur)
            res += x - 1
            cur = nums[i] // x
        return res
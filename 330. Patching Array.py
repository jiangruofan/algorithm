class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        begin = 1
        index = 0
        leng = len(nums)
        while begin <= n:
            if index < leng and nums[index] <= begin:
                begin += nums[index]
                index += 1
            else:
                res += 1
                begin *= 2
        return res
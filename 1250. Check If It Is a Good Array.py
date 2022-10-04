class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        num = nums[0]
        for i in range(len(nums)):
            num = gcd(nums[i], num)
            if num == 1:
                return True
        return False
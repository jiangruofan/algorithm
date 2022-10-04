class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums = set(nums)
        res = 0
        for i in range(1, max1+1):
            x = -1
            for j in range(i, max1+1, i):
                if j in nums:
                    if x == -1:
                        x = j
                    else:
                        x = gcd(x, j)
                    if x == i:
                        res += 1
                        break
        return res
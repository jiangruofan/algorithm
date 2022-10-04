class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(n):
                cnt[nums[i] & nums[j]] += 1
        max1 = 1 << 16
        res = 0
        for val in nums:
            j = max1 - 1 - val
            j1 = j
            while j1 > 0:
                res += cnt[j1]
                j1 = (j1 - 1) & j
            res += cnt[0]

        return res

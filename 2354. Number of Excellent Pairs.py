class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        cnt = Counter()
        for val in nums:
            cnt[val.bit_count()] += 1
        list1 = sorted(cnt.keys())
        r = len(list1) - 1
        l = 0
        totalr = 0
        res = 0
        while l < len(list1):
            while r >= 0 and list1[l] + list1[r] >= k:
                totalr += cnt[list1[r]]
                r -= 1
            res += cnt[list1[l]] * totalr
            l += 1
        return res

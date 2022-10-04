class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7
        res = 0
        n = len(nums1)
        dp = Counter()
        dp[0] = 0
        for i in range(n):
            cnt = Counter()
            cnt[nums1[i]] += 1
            cnt[-nums2[i]] += 1
            for key, val in dp.items():
                cnt[key+nums1[i]] += val
                cnt[key-nums2[i]] += val
                cnt[key+nums1[i]] %= mod
                cnt[key-nums2[i]] %= mod
            dp = cnt
            res += cnt[0]
            res %= mod
        return res
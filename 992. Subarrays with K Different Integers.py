class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l_dic, r_dic = defaultdict(int), defaultdict(int)
        l = r = 0
        leng = len(nums)
        res = 0
        for val in nums:
            l_dic[val] += 1
            r_dic[val] += 1
            while len(l_dic) > k:
                l_dic[nums[l]] -= 1
                if l_dic[nums[l]] == 0:
                    del l_dic[nums[l]]
                l += 1
            while len(r_dic) > k - 1:
                r_dic[nums[r]] -= 1
                if r_dic[nums[r]] == 0:
                    del r_dic[nums[r]]
                r += 1
            res += r - l
        return res


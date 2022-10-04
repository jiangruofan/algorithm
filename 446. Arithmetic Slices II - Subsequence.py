class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        leng = len(nums)
        dic = [defaultdict(int) for _ in range(leng)]
        for i in range(1, leng):
            for j in range(i-1, -1, -1):
                res += dic[j][nums[i]-nums[j]]
                dic[i][nums[i]-nums[j]] += dic[j][nums[i]-nums[j]] + 1
        return res
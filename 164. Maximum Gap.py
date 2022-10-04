class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max1, min1 = max(nums), min(nums)
        bucket_len = max(1, (max1 - min1) // (len(nums) - 1))
        bucket_num = (max1 - min1) // bucket_len + 1
        list1 = [[] for _ in range(bucket_num)]
        for val in nums:
            index = (val - min1) // bucket_len
            list1[index].append(val)
        pre = max(list1[0])
        res = 0
        for i in range(1, len(list1)):
            if list1[i]:
                res = max(res, min(list1[i]) - pre)
                pre = max(list1[i])
        return res


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        list1 = []
        list2 = []
        for i in range(len(nums2)):
            list1.append(nums2[i] - nums1[i])
            list2.append(nums1[i] - nums2[i])
        res = 0
        cnt1 = 0
        cnt2 = 0
        for val in list1:
            cnt1 += val
            if cnt1 < 0:
                cnt1 = 0
            res = max(res, sum1 + cnt1)
        for val in list2:
            cnt2 += val
            if cnt2 < 0:
                cnt2 = 0
            res = max(res, sum2 + cnt2)
        return res


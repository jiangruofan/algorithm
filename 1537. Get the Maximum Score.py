class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7
        common = set(nums1) & set(nums2)
        list1 = []
        list2 = []
        total = 0
        for val in nums1:
            if val in common:
                list1.append(total)
                total = 0
                continue
            total += val
        if total == 0:
            list1.append(0)
        else:
            list1.append(total)

        total = 0
        for val in nums2:
            if val in common:
                list2.append(total)
                total = 0
                continue
            total += val
        if total == 0:
            list2.append(0)
        else:
            list2.append(total)

        res = sum(common)
        for i in range(len(list1)):
            res += max(list1[i], list2[i])
            res %= mod

        return res
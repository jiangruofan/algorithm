from sortedcontainers import SortedSet
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dic = {val:index for index, val in enumerate(nums2)}
        list1 = SortedSet()
        res = 0
        for i in range(len(nums1)):
            index = dic[nums1[i]]
            l = list1.bisect_left(index)
            r = n - 1 - i - (index - l)
            res += l * r
            list1.add(index)
        return res
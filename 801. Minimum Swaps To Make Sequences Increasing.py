class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        pre = [0, 1]
        for i in range(1, len(nums1)):
            new = [float('inf'), float('inf')]
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                new[0] = min(new[0], pre[0])
                new[1] = min(new[1], pre[1] + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                new[0] = min(new[0], pre[1])
                new[1] = min(new[1], pre[0] + 1)
            pre = new
        return min(pre)

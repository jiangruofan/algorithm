class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        num = (m + n + 1) // 2
        l, r = 0, m
        while l <= r:
            mid = (l + r) // 2
            rest = num - mid
            x1 = nums1[mid-1] if mid > 0 else -float('inf')
            x2 = nums1[mid] if mid < m else float('inf')
            x3 = nums2[rest-1] if rest > 0 else -float('inf')
            x4 = nums2[rest] if rest < n else float('inf')
            if x1 > x4:
                r = mid - 1
            elif x3 > x2:
                l = mid + 1
            else:
                max1 = max(x1, x3)
                min1 = min(x2, x4)
                return max1 if (m + n) % 2 == 1 else (max1 + min1) / 2
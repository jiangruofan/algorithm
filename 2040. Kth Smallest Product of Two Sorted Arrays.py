class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def check(limit):
            res = 0
            for val in nums1:
                if val > 0:
                    x = floor(limit / val)
                    res += bisect_right(nums2, x)
                elif val == 0:
                    if limit >= 0:
                        res += len(nums2)
                else:
                    x = ceil(limit / val)
                    res += len(nums2) - bisect_left(nums2, x)
                if res >= k:
                    return True
            return False

        l = -1e10
        r = 1e10
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return int(l)
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = -1
        n = mountain_arr.length()
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if mid == 0:
                mid += 1
            if mid == n - 1:
                mid -= 1
            mid1 = mountain_arr.get(mid)
            left = mountain_arr.get(mid-1)
            right = mountain_arr.get(mid+1)
            if mid1 > left and mid1 > right:
                peak = mid
                break
            elif mid1 > left:
                l = mid + 1
            else:
                r = mid - 1
        if mountain_arr.get(peak) == target:
            return peak
        l, r = 0, peak - 1
        while l <= r:
            mid = (l + r) // 2
            mid1 = mountain_arr.get(mid)
            if mid1 == target:
                return mid
            elif mid1 < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = peak+1, n-1
        while l <= r:
            mid = (l + r) // 2
            mid1 = mountain_arr.get(mid)
            if mid1 == target:
                return mid
            elif mid1 > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
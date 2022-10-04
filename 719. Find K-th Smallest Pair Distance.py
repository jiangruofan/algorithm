class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(dis):
            res = 0
            l = 0
            for i in range(len(nums)):
                while nums[i] - nums[l] > dis:
                    l += 1
                res += i - l
            return res
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            get = check(mid)
            if get < k:
                l = mid + 1
            elif get >= k:
                r = mid
        return l

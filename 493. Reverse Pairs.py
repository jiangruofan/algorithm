class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0

        def cal(nums):
            nonlocal res
            leng = len(nums)
            if leng == 1:
                return nums
            mid = leng // 2
            nums = cal(nums[:mid]) + cal(nums[mid:])
            r = mid
            for i in range(mid):
                while r < leng and nums[r] * 2 < nums[i]:
                    r += 1
                res += r - mid
            new = []
            l, r = 0, mid
            while l < mid and r < leng:
                if nums[l] < nums[r]:
                    new.append(nums[l])
                    l += 1
                else:
                    new.append(nums[r])
                    r += 1
            while l < mid:
                new.append(nums[l])
                l += 1
            while r < leng:
                new.append(nums[r])
                r += 1
            return new

        cal(nums)
        return res
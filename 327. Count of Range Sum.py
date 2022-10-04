class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums = [0] + nums

        res = 0

        def cal(begin, end):
            nonlocal res
            if begin >= end:
                return

            mid = (begin + end) // 2
            cal(begin, mid)
            cal(mid + 1, end)

            l, r = mid + 1, mid + 1
            for i in range(begin, mid + 1):
                while l <= end and nums[l] - nums[i] < lower:
                    l += 1
                while r <= end and nums[r] - nums[i] <= upper:
                    r += 1
                res += r - l

            l, r = begin, mid + 1
            new = []
            while l <= mid and r <= end:
                if nums[l] > nums[r]:
                    new.append(nums[r])
                    r += 1
                else:
                    new.append(nums[l])
                    l += 1

            while l <= mid:
                new.append(nums[l])
                l += 1
            while r <= end:
                new.append(nums[r])
                r += 1
            nums[begin:end + 1] = new

        cal(0, n)
        return res
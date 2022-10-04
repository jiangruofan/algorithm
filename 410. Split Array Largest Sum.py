class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(total):
            cnt = 1
            sum1 = 0
            for val in nums:
                if sum1 + val > total:
                    cnt += 1
                    if cnt > m:
                        return False
                    sum1 = val
                else:
                    sum1 += val
            return True

        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


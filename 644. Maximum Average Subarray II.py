class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        leng = len(nums)
        def check(number:int):
            sum1 = [0] * leng
            min1 = 0
            for i, val in enumerate(nums):
                sum1[i] += val - number + sum1[i-1] if i > 0 else val - number
                if i >= k:
                    min1 = min(min1, sum1[i-k])
                if i >= k-1 and sum1[i] - min1 > 0:
                    return True
            return False
        l ,r = min(nums), max(nums)
        while r - l > 0.00001:
            mid = (l + r) / 2
            if check(mid):
                l = mid
            else:
                r = mid
        return r
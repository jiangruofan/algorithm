class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        max1 = sum1 = index1 = 0
        max2 = sum2 = index2 = 0
        max3 = sum3 = 0
        res = []
        for i in range(2*k, len(nums)):
            sum1 += nums[i - 2 * k]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= 3 * k - 1:
                if sum1 > max1:
                    max1 = sum1
                    index1 = i - 3 * k + 1
                if sum2 + max1 > max2:
                    max2 = sum2 + max1
                    index2 = (index1, i - 2 * k + 1)
                if sum3 + max2 > max3:
                    max3 = sum3 + max2
                    res = [*index2, i - k + 1]
                sum1 -= nums[i - 3 * k + 1]
                sum2 -= nums[ i - 2 * k + 1]
                sum3 -= nums[i - k + 1]
        return res

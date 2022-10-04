class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        presum = res = 0
        for val in satisfaction:
            if presum + val > 0:
                presum += val
                res += presum
            else:
                break
        return res
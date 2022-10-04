class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        l_min = float('inf')
        r_max = -float('inf')
        total = 0
        addtion = -float('inf')
        for i in range(len(nums)-2, -1, -1):
            total += abs(nums[i+1] - nums[i])
            r_max = max(r_max, min(nums[i+1], nums[i]))
            l_min = min(l_min, max(nums[i], nums[i+1]))
            addtion = max(addtion, abs(nums[-1]-nums[i]) - abs(nums[i+1]-nums[i]))
            addtion = max(addtion, abs(nums[0]-nums[i+1]) - abs(nums[i+1]-nums[i]))
        return total + max(addtion, (r_max-l_min) * 2)
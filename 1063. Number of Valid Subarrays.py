class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nums.append(-float('inf'))
        stack = []
        res = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                res += i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        next1 = [n for _ in range(n)]

        stack = []
        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] > val:
                next1[stack[-1]] = i
                stack.pop()
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                if nums[stack[-1]] > threshold / (next1[stack[-1]] - i - 1):
                    return next1[stack[-1]] - i - 1
                stack.pop()
            stack.append(i)

        for val in stack:
            if nums[val] > threshold / next1[val]:
                return next1[val]
        return -1

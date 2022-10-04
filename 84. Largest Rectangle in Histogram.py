class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i, val in enumerate(heights):
            while stack and val < heights[stack[-1]]:
                x = stack.pop()
                res = max(res, heights[x] * (i - stack[-1] - 1))
            stack.append(i)
        return res
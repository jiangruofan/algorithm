class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        for i, val in enumerate(height):
            while stack and val > height[stack[-1]]:
                x = stack.pop()
                if stack:
                    res += (i - stack[-1] - 1) * (min(val, height[stack[-1]]) - height[x])

            stack.append(i)
        return res
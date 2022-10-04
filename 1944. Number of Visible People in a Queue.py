class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(heights)-1, -1, -1):
            cnt= 0
            while stack and stack[-1] < heights[i]:
                cnt += 1
                stack.pop()
            if stack:
                cnt += 1
            res.append(cnt)
            stack.append(heights[i])
        return res[::-1]
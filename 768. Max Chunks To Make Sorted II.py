class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for val in arr:
            max1 = stack[-1] if stack else -1
            judge = False
            while stack and stack[-1] > val:
                stack.pop()
                judge = True
            if judge:
                stack.append(max1)
            else:
                stack.append(val)
        return len(stack)

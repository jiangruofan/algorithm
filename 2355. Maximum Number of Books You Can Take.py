class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        stack = []
        res = 0
        for i, val in enumerate(books):
            while stack and books[stack[-1][0]] >= val - i + stack[-1][0]:
                stack.pop()
            leng = min(i - stack[-1][0] if stack else i + 1, val)
            x = (val + val - leng + 1) * leng // 2
            x1 = stack[-1][1] if stack else 0
            stack.append((i, x + x1))
            res = max(res, x + x1)
        return res

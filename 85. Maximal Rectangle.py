class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def cal(list1):
            list1 = [0] + list1 + [0]
            stack = []
            res = 0
            for i, val in enumerate(list1):
                while stack and val < list1[stack[-1]]:
                    x = stack.pop()
                    res = max(res, list1[x] * (i - stack[-1] - 1))
                stack.append(i)
            return res

        height = list(map(int, matrix[0]))
        res = cal(height)
        for i in range(1, len(matrix)):
            list2 = list(map(int, matrix[i]))
            height = [a + b if b != 0 else 0 for a, b in zip(height, list2)]
            res = max(res, cal(height))
        return res
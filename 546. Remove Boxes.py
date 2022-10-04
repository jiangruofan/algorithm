class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dfs(l, r, num):
            if l == r:
                return num ** 2

            if boxes[l] == boxes[l + 1]:
                return dfs(l + 1, r, num + 1)

            res = num ** 2 + dfs(l + 1, r, 1)

            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[i - 1]:
                    continue
                if boxes[i] == boxes[l]:
                    res = max(res, dfs(l + 1, i - 1, 1) + dfs(i, r, num + 1))
            return res

        return dfs(0, len(boxes) - 1, 1)

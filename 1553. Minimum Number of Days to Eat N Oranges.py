class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(left):
            if left == 0:
                return 0
            if left == 1:
                return 1
            return 1 + min(dfs(left//2) + left % 2, dfs(left//3) + left % 3)
        return dfs(n)
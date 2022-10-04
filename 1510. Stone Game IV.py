class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        set1 = []
        for i in range(1, 10 ** 5):
            if i ** 2 > n:
                break
            set1.append(i ** 2)

        @cache
        def dfs(left):
            if left == 0:
                return False
            for val in set1:
                if val > left:
                    break
                if not dfs(left - val):
                    return True
            return False

        return dfs(n)

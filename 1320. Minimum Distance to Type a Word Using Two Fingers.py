import string


class Solution:
    def minimumDistance(self, word: str) -> int:
        def get(s):
            row = (ord(s) - ord('A')) // 6
            col = (ord(s) - ord('A')) % 6
            return (row, col)

        def cal(s1, s2):
            row1, col1 = get(s1)
            row2, col2 = get(s2)
            return abs(row1 - row2) + abs(col1 - col2)

        leng = len(word)

        @cache
        def dfs(index, f1, f2):
            if index == leng:
                return 0
            res = float('inf')
            res = min(res, cal(f1, word[index]) + dfs(index + 1, word[index], f2))
            res = min(res, cal(f2, word[index]) + dfs(index + 1, f1, word[index]))
            return res

        ans = float('inf')
        for f1 in string.ascii_uppercase:
            for f2 in string.ascii_uppercase:
                ans = min(ans, dfs(0, f1, f2))

        return ans

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            if j + 1 < len(p) and p[j + 1] == '*':
                if dfs(i, j + 2):
                    return True
                if p[j] != '.':
                    for k in range(i, len(s)):
                        if s[k] == p[j]:
                            if dfs(k + 1, j + 2):
                                return True
                        else:
                            break
                else:
                    for k in range(i + 1, len(s) + 1):
                        if dfs(k, j + 2):
                            return True
                return False
            elif i >= len(s):
                return False
            elif p[j] == '.':
                return dfs(i + 1, j + 1)
            else:
                return False if s[i] != p[j] else dfs(i + 1, j + 1)

        return dfs(0, 0)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i:int, j:int):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            if p[j] == '*':
                for k in range(i, len(s)+1):
                    if dfs(k, j+1):
                        return True
                return False
            elif i >= len(s):
                return False
            elif p[j] == '?':
                return dfs(i+1, j+1)
            else:
                return dfs(i+1, j+1) if s[i] == p[j] else False
        return dfs(0, 0)
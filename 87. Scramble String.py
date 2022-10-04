class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(x1, x2, n):
            if s1[x1:x1+n] == s2[x2:x2+n]:
                return True
            if Counter(s1[x1:x1+n]) != Counter(s2[x2:x2+n]):
                return False
            for i in range(1, n):
                if dfs(x1, x2, i) and dfs(x1+i, x2+i, n-i):
                    return True
                if dfs(x1, x2+n-i, i) and dfs(x1+i, x2, n-i):
                    return True
            return False
        return dfs(0, 0, len(s1))
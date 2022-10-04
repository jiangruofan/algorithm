class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if len(s) % 2 == 0:
            judge = True
        else:
            judge = False
            num = Counter(s)
            mid = next((i for i, val in num.items() if val % 2 == 1), -1)

        def dfs(s1, judge):
            leng = len(s1)
            if leng <= 2:
                return 0
            if judge:
                for i in range(leng-1):
                    if s1[i] == s1[-1]:
                        return i + dfs(s1[:i] + s1[i+1:-1], judge)
            else:
                if s1[-1] != mid:
                    for i in range(leng-1):
                        if s1[i] == s1[-1]:
                            return i + dfs(s1[:i] + s1[i+1:-1], judge)
                else:
                    for i in range(leng-1, 0, -1):
                        if s1[i] == s1[0]:
                            return leng - 1 - i + dfs(s1[1:i] + s1[i+1:], judge)
        return dfs(s, judge)
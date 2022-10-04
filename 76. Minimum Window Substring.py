class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        min1 = float('inf')
        res_l = -1
        res_r = -1
        total = len(t)
        l = r = 0
        for r in range(len(s)):
            if s[r] in dic:
                if dic[s[r]] > 0:
                    total -= 1
                dic[s[r]] -= 1
            if total == 0:
                while s[l] not in dic or dic[s[l]] < 0:
                    if dic[s[l]] < 0:
                        dic[s[l]] += 1
                    l += 1
                if r - l + 1 < min1:
                    min1 = r - l + 1
                    res_l = l
                    res_r = r
        return s[res_l: res_r + 1] if res_l != -1 else ""

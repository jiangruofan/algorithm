class Solution:
    def lastSubstring(self, s: str) -> str:
        max1 = max(s)
        res = ""
        for i, val in enumerate(s):
            if val == max1:
                x = s[i:]
                if x > res:
                    res = x
        return res
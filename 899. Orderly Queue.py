class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))

        min1 = min(s)
        res = ""
        for i, val in enumerate(list(s)):
            if val == min1:
                s1 = s[i:] + s[:i]
                if not res:
                    res = s1
                elif s1 < res:
                    res = s1

        return res
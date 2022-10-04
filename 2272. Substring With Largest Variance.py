import string
class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        for s1 in string.ascii_lowercase:
            for s2 in string.ascii_lowercase:
                if s1 == s2:
                    continue
                list1 = []
                for val in s:
                    if val == s1:
                        list1.append(s1)
                    if val == s2:
                        list1.append(s2)
                if not list1:
                    continue
                dp1 = 0 if list1[0] == s2 else 1 #include no s2
                dp2 = -float('inf') if list1[0] == s1 else -1 #include at least one s2
                for i in range(1, len(list1)):
                    if list1[i] == s1:
                        x1 = dp1 + 1
                        x2 = dp2 + 1
                    else:
                        x1 = 0
                        x2 = max(dp1 - 1, dp2 - 1)
                    res = max(res, x2)
                    dp1 = x1
                    dp2 = x2
        return res
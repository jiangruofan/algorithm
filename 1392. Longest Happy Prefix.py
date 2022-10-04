class Solution:
    def longestPrefix(self, s: str) -> str:
        suffix = set()
        p = 131
        mod = 2 ** 64

        sum1 = 0
        pp = 1
        for i in range(len(s) - 1, -1, -1):
            sum1 += ord(s[i]) * pp
            sum1 %= mod
            suffix.add(sum1)
            pp *= p
            pp %= mod

        sum1 = 0
        res = -1
        leng = len(s)
        for i, val in enumerate(s):
            if i == leng - 1:
                break
            sum1 *= p
            sum1 += ord(val)
            sum1 %= mod
            if sum1 in suffix:
                res = i
        return s[:res + 1] if res != -1 else ""

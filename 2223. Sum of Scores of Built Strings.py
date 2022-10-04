class Solution:
    def sumScores(self, s: str) -> int:
        rolling = []
        p_list = []
        p = 1
        mod = 10 ** 9 + 7
        sum1 = 0
        for s1 in s:
            sum1 = sum1 * 131 + ord(s1)
            sum1 %= mod
            rolling.append(sum1)
            p_list.append(p)
            p *= 131
            p %= mod

        def check(begin, leng):
            x = rolling[leng - 1]
            y = rolling[begin + leng - 1] - rolling[begin - 1] * p_list[leng] % mod
            y %= mod
            return x == y

        res = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] != s[0]:
                continue
            l = 0
            r = len(s) - i
            while l < r:
                mid = (l + r + 1) // 2
                if check(i, mid):
                    l = mid
                else:
                    r = mid - 1
            res += l
        res += len(s)
        return res
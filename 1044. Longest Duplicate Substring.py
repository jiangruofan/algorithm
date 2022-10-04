class Solution:
    def longestDupSubstring(self, s: str) -> str:
        leng = len(s)
        p, mod = 131, 2 ** 64
        list1 = [0]
        for i in range(1, leng+1):
            h = list1[-1] * p + ord(s[i-1])
            list1.append(h % mod)
        l, r = 0, leng - 1
        resl = -1
        resr = -1

        def check(x):
            nonlocal resl, resr
            seen = set()
            b = pow(p, x) % mod
            for i in range(x, len(list1)):
                num = (list1[i] - list1[i-x] * b) % mod
                if num in seen:
                    resl = i-x
                    resr = i
                    return True
                seen.add(num)
            return False

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return s[resl:resr]
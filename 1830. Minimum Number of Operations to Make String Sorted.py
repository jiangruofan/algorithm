import string


class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)
        mod = 10 ** 9 + 7
        ret = 0
        multi = [1]

        @cache
        def quickPower(x, y):
            if y == 1:
                return x

            val = quickPower(x, y // 2)
            return val ** 2 % mod if y % 2 == 0 else (val ** 2) * x % mod

        def inv(x):
            return quickPower(x, mod - 2)

        for i in range(1, n + 1):
            multi.append(multi[-1] * i % mod)

        for i, val in enumerate(s):
            total = 0
            for val1 in string.ascii_lowercase:
                if val1 == val:
                    break
                total += cnt[val1]
            num = multi[n - i - 1] * total % mod
            for key, val1 in cnt.items():
                num *= inv(multi[val1])
                num %= mod
            ret += num
            ret %= mod
            cnt[val] -= 1
        return ret

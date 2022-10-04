class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 ** 9 + 7
        res = 0

        def cal(num):
            if num == 1:
                return Counter()
            cnt = Counter()
            for val in range(2, int(num ** 0.5) + 1):
                if num % val == 0:
                    cnt[val] += 1
                    cnt.update(cal(num // val))
                    return cnt
            cnt[num] = 1
            return cnt

        for i in range(1, maxValue + 1):
            x = 1
            dic = cal(i)
            for val in dic.values():
                x *= comb(n + val - 1, n - 1)
                x %= mod
            res += x
        return res % mod

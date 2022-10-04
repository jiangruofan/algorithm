class Solution:

    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        n1 = 1
        while n1 ** 2 < 2 * n:
            x = (2 * n - n1 ** 2) / 2 / n1 + 0.5
            if x  - int(x) == 0:
                res += 1
            n1 += 1
        return res
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        mod = 10 ** 9 + 7
        if primeFactors == 1:
            return 1
        if primeFactors == 2:
            return 2
        x = primeFactors // 3
        if primeFactors % 3 == 0:
            return pow(3, x, mod)
        elif primeFactors % 3 == 1:
            return pow(3, x - 1, mod) * 4 % mod
        else:
            return pow(3, x, mod) * 2 % mod

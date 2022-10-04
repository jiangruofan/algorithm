class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7
        lcm = a * b // gcd(a, b)
        num = lcm // a + lcm // b - 1
        left = n % num
        cur = 0
        a1, b1 = a, b
        while left:
            cur = min(a1, b1)
            if a1 < b1:
                a1 += a
            else:
                b1 += b
            left -= 1
        return (lcm * (n // num) + cur) % mod

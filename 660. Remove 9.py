class Solution:
    def newInteger(self, n: int) -> int:
        res = ''
        while n:
            res += str(n % 9)
            n //= 9
        return int(res[::-1])
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        lower = 10 ** (n - 1)
        upper = 10 ** n - 1
        for val in range(upper, lower - 1, -1):
            x = int(str(val) + str(val)[::-1])
            for i in range(upper, int(sqrt(x)), -1):
                if x % i == 0 and len(str(x // i)) == n:
                    return x % 1337
        return -1
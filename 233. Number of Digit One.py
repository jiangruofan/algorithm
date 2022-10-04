class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 10:
            return 1
        leng = len(str(n))
        dp = [0 for _ in range(leng)]
        dp[1] = 1
        for i in range(2, leng):
            dp[i] = 10 ** (i-1) +  dp[i-1] * 10
        def cal(x):
            if x == 0:
                return 0
            y = 10 ** (len(str(x))-1)
            if str(x)[0] == "1":
                return x % ((x // y) * y) + 1 + x // y * dp[len(str(x))-1] + cal(x % ((x // y) * y))
            return y + x // y * dp[len(str(x))-1] + cal(x % ((x // y) * y))
        return cal(n)
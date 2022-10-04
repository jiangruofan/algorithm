class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        if s[0] == '0':
            return 0
        dp[1] = 1 if s[0] != '*' else 9
        for i in range(2, len(dp)):
            if s[i-1] == '0':
                if s[i-2] != '*':
                    dp[i] = dp[i-2] if 10 <= int(s[i-2:i]) < 27 else 0
                else:
                    dp[i] = 2 * dp[i-2]
                dp[i] %= (10 ** 9 + 7)
            elif s[i-1] != '*':
                if s[i-2] != '*':
                    dp[i] = dp[i-1] + dp[i-2] if 10 < int(s[i-2:i]) < 27 else dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2] * (2 if 0 < int(s[i-1]) < 7 else 1)
                dp[i] %= (10 ** 9 + 7)
            else:
                if s[i-2] == '*':
                    dp[i] = 9 * dp[i-1] + 15 * dp[i-2]
                elif s[i-2] == '1':
                    dp[i] = 9 * dp[i-1] + 9 * dp[i-2]
                elif s[i-2] == '2':
                    dp[i] = 9 * dp[i-1] + 6 * dp[i-2]
                else:
                    dp[i] = 9 * dp[i-1]
                dp[i] %= (10 ** 9 + 7)

        return dp[-1]
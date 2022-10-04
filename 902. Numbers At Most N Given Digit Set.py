class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n1 = str(n)
        dp = [0 for _ in range(len(n1))]
        dp[0] = 1
        res = 0
        for i in range(1, len(n1)):
            dp[i] = dp[i - 1] * len(digits)
            res += dp[i]

        def dfs(index):
            nonlocal res
            if index == len(n1):
                res += 1
                return
            for val in digits:
                if val < n1[index]:
                    res += dp[len(n1) - index - 1]
                elif val > n1[index]:
                    break
                else:
                    dfs(index + 1)

        dfs(0)
        return res
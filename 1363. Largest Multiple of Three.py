class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        n = len(digits)
        dp = [[-float('inf') for _ in range(3)] for _ in range(n)]
        path = defaultdict(lambda: (-1, -1, -1))
        dp[0][digits[0]%3] = 1
        dp[0][0] = 0
        path[(0, digits[0]%3)] = (digits[0], -1, -1)

        for i in range(1, len(digits)):
            for j in range(3):
                if dp[i-1][(j-digits[i]%3)%3] + 1 > dp[i-1][j]:
                    dp[i][j] = dp[i-1][(j-digits[i]%3)%3] + 1
                    path[(i,j)] = (digits[i], i-1, (j-digits[i]%3)%3)
                else:
                    dp[i][j] = dp[i-1][j]
                    path[(i,j)] = (-1, i-1, j)

        res = ""
        cur = (n-1, 0)
        while cur[0] != -1:
            val, x, y = path[cur]
            if val != -1:
                res = str(val) + res
            cur = (x, y)
        if not res:
            return res
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1
        return res[i:] if i < len(res) else "0"

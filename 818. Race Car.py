class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf') for _ in range(target+1)]
        speed = 1
        for i in range(1, target+1):
            if i == 2 ** speed - 1:
                dp[i] = speed
                speed += 1
            else:
                if 2 ** speed - 1 - i < i:
                    dp[i] = speed + 1 + dp[2 ** speed - 1 - i]
                ope = speed - 1
                for j in range(ope):
                    dp[i] = min(dp[i], ope + 2 + j + dp[2 ** j  + i - 2 ** ope])
        return dp[-1]

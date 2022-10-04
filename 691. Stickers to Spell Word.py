class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        leng = len(target)
        dp = [float('inf') for _ in range(1 << leng)]
        dp[0] = 0

        def cal(num, s):
            for s1 in s:
                for i in range(leng):
                    if num & (1 << i) == 0 and s1 == target[i]:
                        num |= 1 << i
                        break
            return num

        for i in range(len(dp)):
            if dp[i] == float('inf'):
                continue
            for val1 in stickers:
                x = cal(i, val1)
                dp[x] = min(dp[x], dp[i] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
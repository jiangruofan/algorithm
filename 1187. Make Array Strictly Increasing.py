class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))
        leng1 = len(arr1)
        leng2 = len(arr2)
        dp = [[float('inf') for _ in range(leng2+1)] for _ in range(leng1)]
        dp[0][0] = 0
        for i in range(1, leng2+1):
            dp[0][i] = 1
        for i in range(1, leng1):
            min1 = float('inf')
            if arr1[i] > arr1[i-1]:
                dp[i][0] = dp[i-1][0]
            for j in range(1, leng2+1):
                dp[i][j] = min1 + 1
                if arr2[j-1] > arr1[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][0] + 1)
                min1 = min(min1, dp[i-1][j])
                if arr1[i] > arr2[j-1]:
                    dp[i][0] = min(dp[i][0], min1)
        return min(dp[-1]) if min(dp[-1]) != float('inf') else -1
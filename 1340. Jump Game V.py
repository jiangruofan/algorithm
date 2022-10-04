class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        list1 = sorted(range(n), key=lambda x: arr[x])
        map1 = [0 for _ in range(n)]
        for i, val in enumerate(list1):
            map1[val] = i

        dp = [1 for _ in range(n)]
        for i, val in enumerate(list1):
            cnt = 0
            for j in range(val+1, min(val+d+1, n)):
                if arr[j] >= arr[val]:
                    break
                cnt = max(cnt, dp[map1[j]])
            for j in range(val-1, max(0, val-d)-1, -1):
                if arr[j] >= arr[val]:
                    break
                cnt = max(cnt, dp[map1[j]])
            dp[i] += cnt

        return max(dp)
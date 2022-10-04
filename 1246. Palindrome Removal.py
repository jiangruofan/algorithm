class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        @cache
        def dfs(l, r):
            if r == l:
                return 1
            if r == l + 1:
                return 1 if arr[l] == arr[r] else 2
            min1 = float('inf')
            if arr[l] == arr[r]:
                min1 = dfs(l+1, r-1)
            for i in range(l, r):
                min1 = min(min1, dfs(l, i) + dfs(i+1, r))
            return min1
        return dfs(0, len(arr)-1)
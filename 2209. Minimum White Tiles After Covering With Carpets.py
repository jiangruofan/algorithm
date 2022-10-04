class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        total = floor.count('1')
        prefix = [0]
        for i in range(n):
            if floor[i] == "1":
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        @cache
        def dfs(index, left):
            if left == 0:
                return 0
            if index >= n:
                return 0
            x = prefix[index + 1] - prefix[index + 1 - carpetLen] if index + 1 - carpetLen >= 0 else prefix[index + 1]
            res = dfs(index + 1, left)
            return max(res, dfs(index + carpetLen, left - 1) + x)

        return total - dfs(0, numCarpets)


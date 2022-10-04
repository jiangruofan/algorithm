class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        num1 = 0
        n = len(piles)
        list1 = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            num1 += len(piles[i])
            list1[i] = num1
        @cache
        def dfs(index, left):
            if left == 0:
                return 0
            if index == n-1:
                return sum(piles[index][:left])
            res = dfs(index+1, left) if left <= list1[index+1] else 0
            total = 0
            for i in range(min(left, len(piles[index]))):
                total += piles[index][i]
                if left-i-1 > list1[index+1]:
                    continue
                res = max(res, total + dfs(index+1, left-i-1))
            return res
        return dfs(0, k)
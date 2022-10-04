class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 1, sum(batteries)
        batteries.sort(reverse=True)
        total = sum(batteries[n:])
        def check(sum1):
            lack = 0
            for i in range(n):
                if sum1 > batteries[i]:
                    lack += sum1 - batteries[i]
            return lack <= total
        while l < r:
            mid = (l + r) // 2 + 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
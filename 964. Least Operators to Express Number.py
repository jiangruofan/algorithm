class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(40))
        cost[0] = 2

        @cache
        def cal(index, total):
            if index > 39:
                return float('inf')
            if total == 0:
                return 0
            if total == 1:
                return cost[index]

            last = total % x
            left = total // x
            return min(last * cost[index] + cal(index + 1, left), (x - last) * cost[index] + cal(index + 1, left + 1))

        return cal(0, target) - 1
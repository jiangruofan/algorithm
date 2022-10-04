class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l = min(sweetness)
        r = sum(sweetness) // (k + 1)

        def check(x):
            total = 0
            sum1 = 0
            for val in sweetness:
                sum1 += val
                if sum1 >= x:
                    total += 1
                    sum1 = 0
            return total >= k + 1

        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

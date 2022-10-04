class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
                if cnt >= k:
                    return False
            return True

        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l
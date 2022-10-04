class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        l, r = 0, 10 ** 8
        n = len(stations)
        def check(limit):
            k1 = k
            for i in range(1, n):
                k1 -= (stations[i] - stations[i-1]) // limit
                if k1 < 0:
                    return False
            return True

        while r - l > 1e-6:
            mid = (l + r) / 2.0
            if check(mid):
                r = mid
            else:
                l = mid
        return r

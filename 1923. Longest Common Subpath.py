class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        mod = (10 ** 9 + 7) * (10 ** 9 + 9)
        p = random.randint(10 ** 6, 10 ** 7)

        def check(leng):
            total = set()
            x = pow(p, leng, mod)
            for k, list1 in enumerate(paths):
                sum1 = 0
                seen = set()
                for j in range(leng):
                    sum1 = sum1 * p + list1[j]
                    sum1 %= mod
                if k == 0 or sum1 in total:
                    seen.add(sum1)
                for i in range(leng, len(list1)):
                    sum1 = sum1 * p - list1[i - leng] * x + list1[i]
                    sum1 %= mod
                    if k == 0 or sum1 in total:
                        seen.add(sum1)

                if not seen:
                    return False
                total = seen
            return True

        l = 0
        r = len(min(paths, key=len))
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

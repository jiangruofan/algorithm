class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        ans = float('inf')
        def check(x, y):
            return (x ** y - 1) // (x - 1)
        for i in range(2, 61):
            l, r = 2, 10 ** 18
            while l <= r:
                mid = (l + r) // 2
                get = check(mid, i)
                if get < n:
                    l = mid + 1
                elif get == n:
                    ans = min(ans, mid)
                    print(mid)
                    break
                else:
                    r = mid - 1
        return str(ans)



'''
1 + k + k ** 2 .... k ** m = n
(k ** m - 1) / (k - 1) = n

'''
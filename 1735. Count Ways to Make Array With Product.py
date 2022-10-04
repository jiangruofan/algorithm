class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        @cache
        def cal(num):
            if num == 1:
                return Counter()
            cnt = Counter()
            for val in range(2, int(sqrt(num))+1):
                if num % val == 0:
                    cnt[val] += 1
                    cnt.update(cal(num//val))
                    return cnt
            cnt[num] += 1
            return cnt

        ans = []
        for n, num in queries:
            x = 1
            cnt = cal(num)
            for val in cnt.values():
                x *= comb(val+n-1, n-1) % mod
            ans.append(x % mod)
        return ans
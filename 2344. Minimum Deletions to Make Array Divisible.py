class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        x = numsDivide[0]
        for i in range(1, len(numsDivide)):
            x = gcd(x, numsDivide[i])

        primes = set()
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                primes.add(i)
                primes.add(x // i)

        cnt = Counter(nums)
        res = 0
        for key in sorted(cnt.keys()):
            if key in primes:
                return res
            res += cnt[key]
        return -1

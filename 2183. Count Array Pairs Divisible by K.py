class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = Counter()
        res = 0
        for val in nums:
            for key, val1 in dic.items():
                if val % key == 0:
                    res += val1
            dic[k//gcd(val, k)] += 1
        return res
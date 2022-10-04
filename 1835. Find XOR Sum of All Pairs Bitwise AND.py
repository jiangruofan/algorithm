class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        cnt = [0 for _ in range(32)]
        for val in arr2:
            x = val
            index = 0
            while x:
                if x & 1:
                    cnt[index] += 1
                index += 1
                x >>= 1

        res = 0
        for val in arr1:
            x = val
            index = 0
            while x:
                if x & 1 and cnt[index] % 2:
                    res ^= 1 << index
                index += 1
                x >>= 1
        return res
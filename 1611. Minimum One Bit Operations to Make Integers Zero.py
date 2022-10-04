class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bit = []
        while n:
            bit.append(1 if n & 1 else 0)
            n >>= 1
        pre = 0
        res = 0
        for i in range(len(bit)-1, -1, -1):
            index = bit[i] ^ pre
            if index:
                res |= 1 << i
            pre = index
        return res
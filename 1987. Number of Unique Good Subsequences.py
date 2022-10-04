class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10 ** 9 + 7
        zero = one = 0
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == "0":
                zero = zero + one + 1
                zero %= mod
            else:
                one = zero + one + 1
                one %= mod
        return one + 1 if "0" in binary else one
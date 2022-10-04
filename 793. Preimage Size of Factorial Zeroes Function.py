class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        x = 1
        while k // x:
            x = x * 5 + 1

        while x:
            if k // x >= 5:
                return 0
            k %= x
            x -= 1
            x //= 5
        return 5

# 1 6 31 156
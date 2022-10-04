class Fancy:

    def __init__(self):
        self.mul = 1
        self.add = 0
        self.nums = []
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        def inverse(x, mod):
            return pow1(x, mod - 2)

        def pow1(x, mod):
            if mod == 1:
                return x
            cnt = pow1(x, mod // 2)
            return cnt ** 2 % self.mod if mod % 2 == 0 else cnt ** 2 * x % self.mod

        self.nums.append((val - self.add) * inverse(self.mul, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add += inc
        self.add %= self.mod

    def multAll(self, m: int) -> None:
        self.mul *= m
        self.add *= m
        self.mul %= self.mod
        self.add %= self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx] * self.mul % self.mod + self.add) % self.mod

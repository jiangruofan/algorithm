class Solution:
    '''
        a   bb   |   b    aa
    x     y      z

        a   b   |   aa   bb
      x   y     z
    '''

    @cache
    def earliestAndLatest(self, n: int, a: int, b: int) -> List[int]:
        if a + b == n + 1:
            return (1, 1)
        if a > b:
            return self.earliestAndLatest(n, b, a)
        if a + b > n + 1:
            return self.earliestAndLatest(n, n - b + 1, n - a + 1)

        min1 = float('inf')
        max1 = -float('inf')
        if b > (n + 1) // 2:
            bb = n + 1 - b
            x, y = a - 1, bb - a - 1
            z = (b - 1 - bb + 1) // 2
            for i in range(x + 1):
                for j in range(y + 1):
                    new = self.earliestAndLatest((n + 1) // 2, i + 1, i + 1 + j + z + 1)
                    min1 = min(min1, new[0] + 1)
                    max1 = max(max1, new[1] + 1)
        else:
            x, y = a - 1, b - a - 1
            for i in range(x + 1):
                for j in range(y + 1):
                    new = self.earliestAndLatest((n + 1) // 2, i + 1, i + 1 + j + 1)
                    min1 = min(min1, new[0] + 1)
                    max1 = max(max1, new[1] + 1)
        return (min1, max1)

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res = []
        for i in range(1, sideLength + 1):
            total = height // sideLength
            total += 1 if i <= height % sideLength else 0
            for j in range(1, sideLength + 1):
                total1 = width // sideLength
                total1 += 1 if j <= width % sideLength else 0
                res.append(total1 * total)

        res.sort(reverse=True)
        return sum(res[:maxOnes])
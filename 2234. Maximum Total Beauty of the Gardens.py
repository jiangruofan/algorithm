class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        num1 = 0
        for i in range(len(flowers) - 1, -1, -1):
            if flowers[i] >= target:
                num1 += 1
            else:
                flowers = flowers[:i + 1]
                break
        if num1 == n:
            return num1 * full
        max1 = flowers[0]
        index = 0
        for i in range(1, len(flowers)):
            if flowers[i] >= target:
                break
            if newFlowers < (flowers[i] - flowers[i - 1]) * i:
                break
            else:
                newFlowers -= (flowers[i] - flowers[i - 1]) * i
                max1 = flowers[i]
                index = i

        complete = 0
        total = min(target - 1, max1 + newFlowers // (index + 1)) * partial
        for i in range(len(flowers) - 1, -1, -1):
            complete += 1
            newFlowers -= target - flowers[i]
            while index >= 1 and newFlowers < 0 or index >= i:
                newFlowers += index * (flowers[index] - flowers[index - 1])
                index -= 1
                max1 = flowers[index]
            if index == 0 and newFlowers < 0:
                break
            if index != -1:
                cnt = newFlowers // (index + 1)
                new = min(target - 1, max1 + cnt)
            else:
                new = 0
            total = max(total, complete * full + new * partial)

        return total + num1 * full

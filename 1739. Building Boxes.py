class Solution:
    def minimumBoxes(self, n: int) -> int:
        total = 0
        index = 0
        cur = 0
        cnt = 0
        while total < n:
            cur += 1
            cnt += cur
            index += cur
            total += cnt
        if total == n:
            return index

        total -= cnt
        index -= cur
        cur = 0
        while total < n:
            cur += 1
            index += 1
            total += cur
        return index
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def check(x:int):
            count = 0
            for i, val in enumerate(statements):
                if (x >> i) & 1 == 1:
                    if any(val1 < 2 and (x >> j) & 1 != val1 for j, val1 in enumerate(val)):
                        return 0
                    count += 1
            return count
        return max(check(i) for i in range(1, 1 << len(statements)))
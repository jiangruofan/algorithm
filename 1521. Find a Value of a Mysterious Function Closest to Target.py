class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = float('inf')
        set1 = set()
        for val in arr:
            new = set()
            for val1 in set1:
                new.add(val1 & val)
                res = min(res, abs(target - (val1 & val)))
            new.add(val)
            res = min(res, abs(target - val))
            set1 = new
        return res
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1
        set1 = set()
        for val in rolls:
            set1.add(val)
            if len(set1) == k:
                res += 1
                set1 = set()
        return res
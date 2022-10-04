class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = defaultdict(set)
        dic[0].add(0)
        for stone in stones:
            for val in dic[stone]:
                for k in (val - 1, val, val + 1):
                    if k > 0:
                        dic[stone+k].add(k)
        return len(dic[stones[-1]]) > 0
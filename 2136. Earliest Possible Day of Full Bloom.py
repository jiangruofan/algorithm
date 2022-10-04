class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        list1 = list(zip(plantTime, growTime))
        list1.sort(key = lambda x:-x[1])
        res = day = 0
        for val in list1:
            day += val[0]
            res = max(res, day + val[1])
        return res
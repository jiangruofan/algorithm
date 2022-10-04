class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum1 = sum(machines)
        leng = len(machines)
        if sum1 % leng:
            return -1
        avg = sum1 // leng
        for i in range(leng):
            machines[i] -= avg
        total = 0
        res = 0
        for val in machines:
            total += val
            res = max(res, abs(total), val)
        return res
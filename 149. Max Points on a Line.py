class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        n = len(points)
        res = 0
        for i in range(n-1):
            dic = Counter()
            for j in range(i+1, n):
                first = points[i]
                second = points[j]
                judge = False
                if first[0] < second[0] and first[1] > second[1]:
                    judge = True
                elif first[0] > second[0] and first[1] < second[1]:
                    judge = True
                x = first[0] - second[0]
                y = first[1] - second[1]
                if x == 0:
                    dic[(0, first[0])] += 1
                    continue
                elif y == 0:
                    dic[(second[1], 0)] += 1
                    continue
                if x < 0 or y < 0:
                    x = abs(x)
                    y = abs(y)
                common = gcd(x, y)
                x //= common
                y //= common
                if judge:
                    dic[(-x, y)] += 1
                else:
                    dic[(x, y)] += 1
            res = max(res, max(dic.values())+1)
        return res
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        list1 = []
        same = 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                same += 1
            else:
                list1.append(atan2(y - location[1], x - location[0]))
        list1.sort()
        n = len(list1)
        list1 += [val + 2 * pi for val in list1]
        angle = angle / 180 * pi
        r = 0
        res = 0
        for i in range(n):
            while r < 2 * n and list1[i] + angle >= list1[r]:
                r += 1
            res = max(res, r - i)
        return res + same

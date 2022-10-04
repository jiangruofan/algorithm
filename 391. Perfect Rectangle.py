class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, x, y, x1, y1 = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        dic = Counter()
        for val in rectangles:
            area += (val[2] - val[0]) * (val[3] - val[1])
            x = min(x, val[0])
            y = min(y, val[1])
            x1 = max(x1, val[2])
            y1 = max(y1, val[3])
            dic[(val[0], val[1])] += 1
            dic[(val[0], val[3])] += 1
            dic[(val[2], val[3])] += 1
            dic[(val[2], val[1])] += 1
        if area != (x1 - x) * (y1 - y):
            return False
        if dic[(x, y)] != 1 or dic[(x, y1)] != 1 or dic[(x1, y)] != 1 or dic[(x1, y1)] != 1:
            return False
        del dic[(x, y)], dic[(x, y1)], dic[(x1, y)], dic[(x1, y1)]
        return not any(val == 1 or val == 3 for val in dic.values())
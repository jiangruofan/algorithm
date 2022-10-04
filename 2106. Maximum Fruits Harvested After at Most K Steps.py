class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        prefix = [[-float('inf'), 0]]
        list1 = [-float('inf')]
        res = 0
        for x, y in fruits:
            prefix.append([x, y + prefix[-1][1]])
            list1.append(x)
            if x == startPos:
                res = y
        l = 0
        r = k
        while r > 0:
            left = startPos - l
            right = startPos + r
            index1 = bisect_left(list1, left)
            index2 = bisect_right(list1, right)
            res = max(res, prefix[index2-1][1] - prefix[index1-1][1])
            l += 1
            r = k - 2 * l
        l = k
        r = 0
        while l > 0:
            left = startPos - l
            right = startPos + r
            index1 = bisect_left(list1, left)
            index2 = bisect_right(list1, right)
            res = max(res, prefix[index2-1][1] - prefix[index1-1][1])
            r += 1
            l = k - 2 * r
        return res
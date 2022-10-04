class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        res = 0
        leng = len(slices)
        list1 = [Node(val) for val in slices]
        list1[0].l = list1[-1]
        list1[0].r = list1[1]
        list1[-1].l = list1[-2]
        list1[-1].r = list1[0]
        for i in range(1, leng - 1):
            list1[i].l = list1[i - 1]
            list1[i].r = list1[i + 1]
        heapify(list1)
        for _ in range(leng // 3):
            while list1[0].judge:
                heappop(list1)
            node = heappop(list1)
            res += node.val
            node.val = node.l.val + node.r.val - node.val
            node.l.judge = True
            node.r.judge = True
            node.l = node.l.l
            node.l.r = node
            node.r = node.r.r
            node.r.l = node
            heappush(list1, node)
        return res


class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
        self.judge = False

    def __lt__(self, other):
        return self.val > other.val
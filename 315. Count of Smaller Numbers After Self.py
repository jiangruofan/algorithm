class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def add(node, val):
            if node.begin == node.end:
                node.total += 1
                return 0
            mid = (node.begin + node.end) // 2
            if not node.left:
                node.left = node1(node.begin, mid)
            if not node.right:
                node.right = node1(mid + 1, node.end)

            if val <= mid:
                ans = add(node.left, val)
            else:
                ans = node.left.total + add(node.right, val)

            node.total = node.left.total + node.right.total
            return ans

        root = node1(min(nums), max(nums))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(add(root, nums[i]))
        return res[::-1]


class node1:
    def __init__(self, begin, end, total=0, left=None, right=None):
        self.begin = begin
        self.end = end
        self.total = total
        self.left = left
        self.right = right
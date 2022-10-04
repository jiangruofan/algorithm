class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def build(l, r):
            if l == r:
                return node1(l, r, s[l], s[r], 1, 1, 1)
            mid = (l + r) // 2
            node_l = build(l, mid)
            node_r = build(mid+1, r)
            prefix = node_l.prefix
            suffix = node_r.suffix
            if node_l.r == node_r.l:
                if node_l.suffix == node_l.end - node_l.begin + 1:
                    prefix = node_l.suffix + node_r.prefix
                if node_r.prefix == node_r.end - node_r.begin + 1:
                    suffix = node_r.prefix + node_l.suffix
                return node1(l, r, node_l.l, node_r.r, prefix, suffix, max(prefix, suffix, node_l.max1, node_r.max1, node_l.suffix + node_r.prefix), node_l, node_r)
            else:
                return node1(l, r, node_l.l, node_r.r, prefix, suffix, max(node_l.max1, node_r.max1), node_l, node_r)


        def update(node, index, val, l, r):
            if node.begin == node.end == index:
                node.l = val
                node.r = val
                return
            mid = (l + r) // 2
            if index <= mid:
                update(node.left, index, val, l, mid)
            else:
                update(node.right, index, val, mid+1, r)
            node_l = node.left
            node_r = node.right
            prefix = node_l.prefix
            suffix = node_r.suffix
            if node_l.r == node_r.l:
                if node_l.suffix == node_l.end - node_l.begin + 1:
                    prefix = node_l.suffix + node_r.prefix
                if node_r.prefix == node_r.end - node_r.begin + 1:
                    suffix = node_r.prefix + node_l.suffix
                max1 = max(prefix, suffix, node_l.max1, node_r.max1, node_l.suffix + node_r.prefix)
            else:
                max1 = max(node_l.max1, node_r.max1)
            node.l = node_l.l
            node.r = node_r.r
            node.prefix = prefix
            node.suffix = suffix
            node.max1 = max1

        root = build(0, len(s) - 1)
        res = []
        for i in range(len(queryCharacters)):
            update(root, queryIndices[i], queryCharacters[i], 0, len(s) - 1)
            res.append(root.max1)
        return res

class node1:
    def __init__(self, begin, end, l, r, prefix, suffix, max1, left=None, right=None):
        self.begin = begin
        self.end = end
        self.l = l
        self.r = r
        self.prefix = prefix
        self.suffix = suffix
        self.max1 = max1
        self.left = left
        self.right = right
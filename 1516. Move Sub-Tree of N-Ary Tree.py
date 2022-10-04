"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        root = Node(-1, [root])
        pfa = None
        qfa = None
        judge = False
        def dfs(node, fa):
            nonlocal pfa, qfa, judge
            x = 0
            for child in node.children:
                x |= dfs(child, node)
            if node.val == q.val:
                qfa = fa
                return 1
            elif node.val == p.val:
                pfa = fa
                if x:
                    judge = True
            return x
        dfs(root, None)

        if pfa != q and not judge:
            q.children.append(p)
            pfa.children.remove(p)
        if judge:
            qfa.children.remove(q)
            q.children.append(p)
            index = pfa.children.index(p)
            pfa.children[index] = q
        return root.children[0]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        def dfs(node, bros):
            new = TreeNode(node.val)
            if node.children:
                x = deque(node.children)
                child = x.popleft()
                new.left = dfs(child, x)
            if bros:
                x = bros.popleft()
                new.right = dfs(x, bros)
            return new

        return dfs(root, deque())

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None

        def dfs(node, fa):
            new = Node(node.val, [])
            fa.children.append(new)
            if node.right:
                dfs(node.right, fa)
            if node.left:
                dfs(node.left, new)

        res = Node(data.val, [])
        if data.left:
            dfs(data.left, res)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
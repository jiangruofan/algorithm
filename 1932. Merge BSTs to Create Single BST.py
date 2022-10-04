# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaves = set()
        roots = {}
        for node in trees:
            if node.left:
                leaves.add(node.left.val)
            if node.right:
                leaves.add(node.right.val)
            roots[node.val] = node

        if len(roots) == 1:
            return trees[0]

        pre = -float('inf')

        def dfs(node):
            nonlocal pre
            if not node:
                return True

            if not node.left and not node.right and node.val in roots:
                node.left = roots[node.val].left
                node.right = roots[node.val].right
                del roots[node.val]

            if not dfs(node.left):
                return False

            if node.val <= pre:
                return False
            pre = node.val

            return dfs(node.right)

        for key in roots:
            if key not in leaves:
                return roots[key] if dfs(roots[key]) and len(roots) == 1 else None

        return None
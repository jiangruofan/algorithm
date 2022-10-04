# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:

        def dfs(node):
            if node.val == 0:
                return (0, 1)
            elif node.val == 1:
                return (1, 0)
            elif node.val == 5:
                not1, yes1 = dfs(node.left if node.left else node.right)
                return (yes1, not1)

            not1, yes1 = dfs(node.left)
            not2, yes2 = dfs(node.right)
            if node.val == 2:
                return (not1 + not2, min(not1 + yes2, not2 + yes1, yes1 + yes2))
            elif node.val == 3:
                return (min(not1 + yes2, not2 + yes1, not1 + not2), yes1 + yes2)
            else:
                return (min(not1 + not2, yes1 + yes2), min(not1 + yes2, yes1 + not2))

        not1, yes1 = dfs(root)
        return yes1 if result else not1

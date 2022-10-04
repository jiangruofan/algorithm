# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 0 represents no monitor, 1 represents monitor, 2 represents camera
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 1
            state1 = dfs(node.left)
            state2 = dfs(node.right)
            if state1 == 0 or state2 == 0:
                res += 1
                return 2
            elif state1 == 2 or state2 == 2:
                return 1
            else:
                return 0

        new_root = TreeNode(left=root)
        dfs(new_root)
        return res

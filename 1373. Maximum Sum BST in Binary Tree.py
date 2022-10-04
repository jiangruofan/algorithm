class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return (True, -float('inf'), float('inf'), 0)
            judge1, min1, max1, total1 = dfs(node.left)
            judge2, min2, max2, total2 = dfs(node.right)
            if judge1 and judge2:
                if not node.left or max1 < node.val:
                    if not node.right or node.val < min2:
                        total = total1 + total2 + node.val
                        res = max(res, total)
                        left = min1 if node.left else node.val
                        right = max2 if node.right else node.val
                        return (True, left, right, total)
            return (False, -1, -1, -1)

        dfs(root)
        return res
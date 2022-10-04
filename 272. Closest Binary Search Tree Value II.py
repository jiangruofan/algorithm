# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        list1 = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            list1.append(node.val)
            dfs(node.right)

        dfs(root)
        list1 = [-float('inf')] + list1 + [float('inf')]
        pos = bisect_right(list1, target)
        ans = []
        l = pos - 1
        r = pos
        while k:
            if target - list1[l] < list1[r] - target:
                ans.append(list1[l])
                l -= 1
            else:
                ans.append(list1[r])
                r += 1
            k -= 1
        return ans
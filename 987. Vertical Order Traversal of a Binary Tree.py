# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(lambda: defaultdict(list))
        def dfs(node, r, c):
            if not node:
                return
            dic[c][r].append(node.val)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        dfs(root, 0, 0)
        res = []
        for key in sorted(dic.keys()):
            list1 = []
            for key1 in sorted(dic[key]):
                list1.extend(sorted(dic[key][key1]))
            res.append(list1)
        return res
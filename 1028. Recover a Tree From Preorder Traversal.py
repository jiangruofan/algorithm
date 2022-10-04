# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal += "-"
        nodes = deque()
        cnt = 0
        s = ""
        index = 0
        while index < len(traversal):
            if traversal[index].isdigit():
                s += traversal[index]
                index += 1
            else:
                nodes.append((cnt, int(s)))
                cnt = 0
                s = ""
                while index < len(traversal):
                    if traversal[index] == "-":
                        cnt += 1
                    else:
                        break
                    index += 1

        def dfs(depth):
            if not nodes or nodes[0][0] != depth:
                return None

            if nodes[0][0] == depth:
                root = TreeNode(nodes[0][1])
                nodes.popleft()
                root.left = dfs(depth + 1)
                root.right = dfs(depth + 1)
                return root

        return dfs(0)

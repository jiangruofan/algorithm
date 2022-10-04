# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        def dfs(s):
            s1 = s
            s = list(s)
            if "+" not in s and "-" not in s and "*" not in s and "/" not in s:
                return Node(s1)
            cnt = 0
            sign1 = ""
            which1 = -1
            sign2 = ""
            whcih2 = -1
            for i, val in enumerate(s):
                if val == "(":
                    cnt += 1
                elif val == ")":
                    cnt -= 1
                elif val == "+" or val == "-" :
                    if cnt == 0:
                        if sign1 and sign1 == "+":
                            continue
                        sign1 = val
                        which1 = i
                elif val == "*" or val == "/":
                    if cnt == 0:
                        sign2 = val
                        whcih2 = i

            node = Node(sign1 if sign1 else sign2)
            leng = which1 if which1 != -1 else whcih2
            if node.val == "":
                return dfs(s1[1:-1])
            node.left = dfs(s1[:leng])
            node.right = dfs(s1[leng+1:])
            return node

        return dfs(s)
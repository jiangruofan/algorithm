# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        deq = deque([root])
        res = ""
        while deq:
            x = deq.popleft()
            if not x:
                res += "#,"
            else:
                res += str(x.val) + ","
                deq.append(x.left)
                deq.append(x.right)
        return res

    def deserialize(self, data):
        list1 = data.split(",")[:-1]
        if list1[0] == "#":
            return None
        root = TreeNode(int(list1[0]))
        deq = deque([root])
        i = 1
        while deq:
            x = deq.popleft()
            if list1[i] != "#":
                x.left = TreeNode(int(list1[i]))
                deq.append(x.left)
            i += 1
            if list1[i] != "#":
                x.right = TreeNode(int(list1[i]))
                deq.append(x.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
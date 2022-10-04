"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        s = str(root.val) + "["
        for child in root.children:
            s += self.serialize(child)
            s += " "
        s += "]"
        return s

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data1 = data
        data = list(data)
        index = 0
        for i in range(len(data)):
            if not data[i].isdigit():
                index = i
                break
        root = Node(int(data1[:index]), [])

        list1 = []
        cnt = 0
        s = ""
        for i in range(index + 1, len(data) - 1):
            if data[i] == "[":
                cnt += 1
                s += "["
            elif data[i] == "]":
                cnt -= 1
                s += "]"
            elif data[i] == " ":
                if cnt == 0:
                    list1.append(s)
                    s = ""
                else:
                    s += " "
            else:
                s += data[i]

        for node in list1:
            root.children.append(self.deserialize(node))
        return root


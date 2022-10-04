class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = trie()
        for word in paths:
            root.add(word)

        dic = Counter()

        def dfs(node):
            if not node.children:
                return ""

            res = []
            for s in node.children:
                res.append(s + "#" + dfs(node.children[s]) + "#")
            res.sort()
            res = "".join(res)

            node.encode = res
            dic[res] += 1
            return res

        for val in root.children:
            dfs(root.children[val])

        ret = []

        def dfs1(node, path):
            if dic[node.encode] > 1:
                return

            ret.append(path[::])
            for val in node.children:
                path.append(val)
                dfs1(node.children[val], path)
                path.pop()

        for val in root.children:
            dfs1(root.children[val], [val])

        return ret


class trie:

    def __init__(self):
        self.children = defaultdict(trie)
        self.encode = ""

    def add(self, words):
        cur = self
        for word in words:
            cur = cur.children[word]
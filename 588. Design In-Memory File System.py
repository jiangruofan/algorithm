class FileSystem:

    def __init__(self):
        self.root = trie()

    def ls(self, path: str) -> List[str]:
        return self.root.is1(path)

    def mkdir(self, path: str) -> None:
        self.root.addDir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.root.addContent(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        return self.root.read(filePath)


class trie:
    def __init__(self):
        self.dire = defaultdict(trie)
        self.file = defaultdict(str)

    def addDir(self, path):
        x = path.split('/')[1:]
        cur = self
        for s in x:
            cur = cur.dire[s]

    def addContent(self, path, content):
        x = path.split('/')[1:]
        cur = self
        for i in range(len(x) - 1):
            cur = cur.dire[x[i]]
        cur.file[x[-1]] += content

    def is1(self, path):
        if path == '/':
            return sorted(list(self.dire.keys()) + list(self.file.keys()))
        x = path.split('/')[1:]
        cur = self
        for i in range(len(x) - 1):
            cur = cur.dire[x[i]]
        if x[-1] in cur.file:
            return [x[-1]]
        else:
            cur = cur.dire[x[-1]]
            ans = []
            ans.extend(list(cur.dire.keys()))
            ans.extend(list(cur.file.keys()))
            ans.sort()
            return ans

    def read(self, path):
        x = path.split('/')[1:]
        cur = self
        for i in range(len(x) - 1):
            cur = cur.dire[x[i]]
        return cur.file[x[-1]]
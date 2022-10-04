class StreamChecker:

    def __init__(self, words: List[str]):
        self.node = trie()
        for word in words:
            self.node.add(word[::-1])
        self.s = ""

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        cur = self.node
        for s1 in self.s:
            if s1 not in cur.children:
                break
            cur = cur.children[s1]
            if cur.judge:
                return True
        return False


class trie:

    def __init__(self):
        self.children = defaultdict(trie)
        self.judge = False

    def add(self, word):
        cur = self
        for s in word:
            cur = cur.children[s]
        cur.judge = True



class WordFilter:

    def __init__(self, words: List[str]):
        self.node = Trie()
        for weight, word in enumerate(words):
            for i in range(1, len(word)+1):
                self.node.add(word[-i:] + "#" + word, weight)


    def f(self, prefix: str, suffix: str) -> int:
        word = suffix + "#" + prefix
        cur = self.node
        for s in word:
            cur = cur.children[s]
        return cur.weight



class Trie:

    def __init__(self):
        self.children = defaultdict(Trie)
        self.weight = -1

    def add(self, word, weight):
        cur = self
        judge = False
        for s in word:
            cur = cur.children[s]
            if judge:
                cur.weight = weight
            if s == "#":
                judge = True


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.transform1 = {}
        self.transform2 = defaultdict(set)
        leng = len(keys)
        for i in range(leng):
            self.transform1[keys[i]] = values[i]
            self.transform2[values[i]].add(keys[i])
        self.node = Trie()
        for word in dictionary:
            self.node.add(word)

    def encrypt(self, word1: str) -> str:
        res = ""
        for s in word1:
            if s not in self.transform1:
                return ""
            res += self.transform1[s]
        return res

    def decrypt(self, word2: str) -> int:
        list1 = deque()
        for i in range(0, len(word2), 2):
            list1.append(word2[i:i + 2])

        def cal(words, node):
            if not words:
                return 1 if node.judge else 0
            res = 0
            for child in self.transform2[words[0]]:
                if child not in node.children:
                    continue
                x = words.popleft()
                res += cal(words, node.children[child])
                words.appendleft(x)
            return res

        return cal(list1, self.node)


class Trie:

    def __init__(self):
        self.children = defaultdict(Trie)
        self.judge = False

    def add(self, word):
        cur = self
        for s in word:
            cur = cur.children[s]
        cur.judge = True

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
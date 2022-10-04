class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = node()
        self.root.add(sentences, times)
        self.curNode = self.root
        self.curWord = ""


    def input(self, c: str) -> List[str]:
        if c == "#":
            self.curNode.times += 1
            self.curNode.word = self.curWord
            self.curWord = ""
            self.curNode = self.root
            return []
        self.curWord += c
        self.curNode = self.curNode.children[c]
        cur = self.curNode
        res = []
        ans = []
        def dfs(node1):
            if node1.word:
                heappush(res, (-node1.times, node1.word))
            if not node1.children:
                return
            for s in node1.children:
                dfs(node1.children[s])
        if cur.children:
            dfs(cur)
        elif cur.word:
            heappush(res, (-cur.times, cur.word))
        k = 3
        while res and k != 0:
            ans.append(heappop(res)[1])
            k -= 1
        return ans

class node:

    def __init__(self):
        self.children = defaultdict(node)
        self.times = 0
        self.word = ""

    def add(self, sentences, times):
        n = len(times)
        for i in range(n):
            word = sentences[i]
            t = times[i]
            cur = self
            for s in word:
                cur = cur.children[s]
            cur.times += t
            cur.word = word

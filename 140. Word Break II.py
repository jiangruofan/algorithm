class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        node = node1()
        for s1 in wordDict:
            node.add(s1)
        node.dfs(s, 0, '')
        return node.res

class node1:
    def __init__(self):
        self.children = defaultdict(node1)
        self.isword = False
        self.word = ''
        self.res = []

    def add(self, str1):
        cur = self
        for s in str1:
            cur = cur.children[s]
        cur.isword = True
        cur.word = str1

    def dfs(self, s, index, path):
        if index == len(s):
            self.res.append(path[1:])
            return
        cur = self
        for i in range(index, len(s)):
            if cur.children[s[i]].isword:
                self.dfs(s, i+1, path + ' ' + cur.children[s[i]].word)
            cur = cur.children[s[i]]
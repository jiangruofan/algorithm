class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        node = node1()
        words.sort(key=len)
        ans = []
        for s in words:
            if not s:
                continue
            if node.check(s, 0):
                ans.append(s)
            else:
                node.add(s)
        return ans


class node1:
    def __init__(self):
        self.children = defaultdict(node1)
        self.isword = False

    def add(self, s):
        cur = self
        for val in s:
            cur = cur.children[val]
        cur.isword = True

    @cache
    def check(self, s, index):
        if index == len(s):
            return True
        cur = self
        for i in range(index, len(s)):
            if s[i] not in cur.children:
                return False
            if cur.children[s[i]].isword and self.check(s, i + 1):
                return True
            cur = cur.children[s[i]]
        return False
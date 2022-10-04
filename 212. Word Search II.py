class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = node1()
        for word in words:
            root.add(word)
        m,n = len(board), len(board[0])
        res = []
        def dfs(x, y, node):
            if board[x][y] in node.children:
                if node.children[board[x][y]].judge:
                    node.children[board[x][y]].judge = False
                    res.append(node.children[board[x][y]].words)
                for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and board[x1][y1] != "#":
                        sign = board[x][y]
                        board[x][y] = "#"
                        dfs(x1, y1, node.children[sign])
                        board[x][y] = sign
                if not node.children[board[x][y]].children and not node.children[board[x][y]].judge:
                    del node.children[board[x][y]]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res

class node1:
    def __init__(self):
        self.children = defaultdict(node1)
        self.judge = False
        self.words = ""

    def add(self, s):
        cur = self
        for s1 in s:
            cur = cur.children[s1]
        cur.judge = True
        cur.words = s
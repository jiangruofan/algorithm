class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1 for _ in range(n)] for _ in range(33)]
        for i, val in enumerate(parent):
            self.dp[0][i] = val

        for i in range(1, 33):
            for j in range(n):
                if self.dp[i - 1][j] != -1:
                    self.dp[i][j] = self.dp[i - 1][self.dp[i - 1][j]]

    def getKthAncestor(self, node: int, k: int) -> int:
        index = 0
        while k:
            if k & 1:
                node = self.dp[index][node]
                if node == -1:
                    break
            k >>= 1
            index += 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent) 1101
# param_1 = obj.getKthAncestor(node,k)
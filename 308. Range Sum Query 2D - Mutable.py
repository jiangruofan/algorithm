class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.r = len(matrix)
        self.c = len(matrix[0])
        self.border = self.r * self.c
        self.bit1 = [0 for _ in range(self.border + 1)]
        for i in range(self.r):
            for j in range(self.c):
                self.add(self.transform(i, j), matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        self.add(self.transform(row, col), val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.query(self.transform(i, col2)) - self.query(self.transform(i, col1) - 1)
        return res

    def transform(self, x, y):
        return x * self.c + y + 1

    def lowbit(self, x):
        return x & (-x)

    def add(self, pos, val):
        while pos <= self.border:
            self.bit1[pos] += val
            pos += self.lowbit(pos)

    def query(self, pos):
        res = 0
        while pos > 0:
            res += self.bit1[pos]
            pos -= self.lowbit(pos)
        return res

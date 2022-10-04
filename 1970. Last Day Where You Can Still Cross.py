class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        fa = {}
        waters = set()
        for i in range(row * col):
            fa[i] = i
            waters.add(i)
        fa[-1] = -1
        fa[row * col] = row * col

        def find(x):
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 == fa2:
                return
            if fa1 < fa2:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2

        def transform(x, y):
            return x * col + y

        '''
        waters = set()
        for x, y in cells:
            waters.add(transform(x-1, y-1))


        for i in range(row):
            for j in range(col):
                node = transform(i, j)
                if node in waters:
                    continue
                if node < col:
                    union(-1, node)
                if row * col - col <= node < row * col:
                    union(node, row*col)
                for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= x < row and 0 <= y < col and transform(x, y) not in waters:
                        union(node, transform(x, y))
        '''

        for i in range(len(cells) - 1, -1, -1):
            x = cells[i][0] - 1
            y = cells[i][1] - 1
            node = transform(x, y)
            waters.remove(node)
            if node < col:
                union(-1, node)
            if row * col - col <= node < row * col:
                union(node, row * col)
            for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x1 < row and 0 <= y1 < col and transform(x1, y1) not in waters:
                    union(node, transform(x1, y1))
            if find(-1) == find(row * col):
                return i

class Excel:

    def __init__(self, height: int, width: str):
        self.list1 = [[0 for _ in range(ord(width) - ord('A') + 1)] for _ in range(height + 1)]
        self.expression = [['' for _ in range(ord(width) - ord('A') + 1)] for _ in range(height + 1)]

    def set(self, row: int, column: str, val: int) -> None:
        self.list1[row][ord(column) - ord('A')] = val
        self.expression[row][ord(column) - ord('A')] = ''

    def get(self, row: int, column: str) -> int:
        if not self.expression[row][ord(column) - ord('A')]:
            return self.list1[row][ord(column) - ord('A')]

        res = 0
        for val in self.expression[row][ord(column) - ord('A')]:
            s = val.split(':')
            if len(s) == 1:
                res += self.get(int(s[0][1:]), s[0][:1])
            else:
                topx = int(s[0][1:])
                topy = ord(s[0][:1]) - ord('A')
                downx = int(s[1][1:])
                downy = ord(s[1][:1]) - ord('A')
                for i in range(topx, downx + 1):
                    for j in range(topy, downy + 1):
                        res += self.get(i, chr(j + ord('A')))
        return res

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.expression[row][ord(column) - ord('A')] = numbers
        return self.get(row, column)



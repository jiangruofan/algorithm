class TextEditor:

    def __init__(self):
        self.l = []
        self.r = []


    def addText(self, text: str) -> None:
        for s in text:
            self.l.append(s)


    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.l and cnt < k:
            self.l.pop()
            cnt += 1
        return cnt


    def cursorLeft(self, k: int) -> str:
        while self.l and k:
            self.r.append(self.l.pop())
            k -= 1
        if len(self.l) <= 10:
            return "".join(self.l)
        else:
            return "".join(self.l[-10:])


    def cursorRight(self, k: int) -> str:
        while self.r and k:
            self.l.append(self.r.pop())
            k -= 1
        if len(self.l) <= 10:
            return "".join(self.l)
        else:
            return "".join(self.l[-10:])


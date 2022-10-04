# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = ['' for _ in range(4)]
        self.index = 0
        self.size = 0

    def read(self, buf, n):
        i = 0
        while i < n:
            while self.index < self.size and i < n:
                buf[i] = self.buffer[self.index]
                i += 1
                self.index += 1
            if i < n:
                self.size = read4(self.buffer)
                self.index = 0
                if self.size == 0:
                    break
        return i
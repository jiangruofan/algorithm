class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []


    def addNum(self, num: int) -> None:
        if not self.left:
            heappush(self.left, -num)
            return
        if self.right and num > self.right[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        if len(self.left) - len(self.right) > 1:
            heappush(self.right, -heappop(self.left))
        elif len(self.right) - len(self.left) > 0:
            heappush(self.left, -heappop(self.right))


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]

from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.list1 = SortedList()


    def book(self, start: int, end: int) -> int:
        self.list1.add((start, 1))
        self.list1.add((end, -1))
        cnt = 0
        res = 0
        for i in range(len(self.list1)):
            cnt += 1 if self.list1[i][1] == 1 else -1
            res = max(res, cnt)
        return res



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        list1 = []
        for val in schedule:
            for val1 in val:
                list1.append([val1.start, val1.end, val1])
        list1.sort(key = lambda x : (x[0], x[1]))
        res = []
        save = []
        for x, y, node in list1:
            if save:
                if x <= save[-1][1] and y > save[-1][1]:
                    save[-1][1] = y
                    continue
                elif x > save[-1][1]:
                    node.start = save[-1][1]
                    node.end = x
                    res.append(node)
                    save.append([x, y])
            else:
                save.append([x, y])
        return res
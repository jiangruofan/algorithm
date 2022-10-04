# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1 = topRight.x
        y1 = topRight.y
        x2 = bottomLeft.x
        y2 = bottomLeft.y
        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft):
            return 0
        if x1 == x2 and y1 == y2:
            return 1
        x, y = (x1+x2)//2, (y1+y2)//2
        return self.countShips(sea, Point(x, y), Point(x2, y2)) + self.countShips(sea, Point(x1, y1), Point(x+1, y+1)) + self.countShips(sea, Point(x, y1), Point(x2, y+1)) + self.countShips(sea, Point(x1, y), Point(x+1, y2))
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        leng = len(distance)
        if leng < 4:
            return False
        index = 2
        while index < leng and distance[index] > distance[index-2]:
            index += 1
        if index == leng:
            return False
        x = distance[index-2]
        y = distance[index-4] if index >= 4 else 0
        if distance[index] >= x - y:
            distance[index-1] -= distance[index-3] if index >= 3 else 0
        index += 1
        while index < leng and distance[index] < distance[index-2]:
            index += 1
        return index != leng
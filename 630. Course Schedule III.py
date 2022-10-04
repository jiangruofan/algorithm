class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        res = 0
        heap = []
        total = 0
        for x, y in courses:
            heappush(heap, -x)
            total += x
            if total <= y:
                res += 1
            else:
                total -= -heappop(heap)
        return res

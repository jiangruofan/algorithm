class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = [(0, cars[-1][1])]
        res = [-1 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            if cars[i][1] <= stack[0][1]:
                stack = [(0, cars[i][1])]
                continue

            dis = cars[i + 1][0] - cars[i][0]
            total = 0
            v, t = stack[-1][1], stack[-1][0]
            stack.pop()
            while stack:
                if (stack[-1][0] - t) * v + total + dis >= stack[-1][0] * cars[i][1]:
                    total += (stack[-1][0] - t) * v
                    v, t = stack[-1][1], stack[-1][0]
                    stack.pop()
                else:
                    break

            dt = (dis - (t * cars[i][1] - total)) / (cars[i][1] - v)
            res[i] = t + dt
            stack.append((t + dt, v))
            stack.append((0, cars[i][1]))
        return res

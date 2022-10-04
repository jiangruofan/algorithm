class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dic = {"rook": ((1, 0), (-1, 0), (0, 1), (0, -1)),
               "bishop": ((-1, -1), (-1, 1), (1, 1), (1, -1)),
               "queen": ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1))
               }

        def getstatus(name, x, y):
            res = [(x, y, 0, 0, 0)]
            for (dirx, diry), steps in product(dic[name], range(1, 8)):
                x1 = x + dirx * steps
                y1 = y + diry * steps
                if 1 <= x1 <= 8 and 1 <= y1 <= 8:
                    res.append((x, y, dirx, diry, steps))
            return res

        def check(status):
            for i in range(8):
                seen = set()
                for x, y, dirx, diry, steps in status:
                    step = min(i, steps)
                    x1 = x + dirx * step
                    y1 = y + diry * step
                    if (x1, y1) in seen:
                        return False
                    seen.add((x1, y1))
            return True

        ans = 0
        for status in product(*[getstatus(pieces[i], positions[i][0], positions[i][1]) for i in range(len(pieces))]):
            if check(status):
                ans += 1
        return ans

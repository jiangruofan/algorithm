class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        leng = len(regular)
        x, y = regular[0], expressCost + express[0]
        res = [min(x, y)]
        for i in range(1, leng):
            x1 = min(x + regular[i], y + regular[i])
            y1 = min(x + express[i] + expressCost, y + express[i])
            res.append(min(x1, y1))
            x, y = x1, y1
        return res
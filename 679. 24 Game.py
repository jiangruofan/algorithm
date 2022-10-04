class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24) < 10 ** (-6)

        for _ in range(len(cards)):
            x = cards.pop(0)
            for _ in range(len(cards)):
                y = cards.pop(0)
                if y == 0:
                    list1 = (x + y, x - y, x * y)
                else:
                    list1 = (x + y, x - y, x * y, x / y)
                for val in list1:
                    cards.append(val)
                    if self.judgePoint24(cards):
                        return True
                    cards.pop()
                cards.append(y)
            cards.append(x)
        return False
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total = 0
        maxCashBack = 0
        maxCost = 0
        for cost, cashBack in transactions:
            if cost > cashBack:
                total += cost - cashBack
                maxCashBack = max(maxCashBack, cashBack)
            else:
                maxCost = max(maxCost, cost)
        return total + max(maxCashBack, maxCost)

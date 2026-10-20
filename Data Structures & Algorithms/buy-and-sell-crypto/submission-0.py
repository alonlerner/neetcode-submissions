class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpri = prices[0]
        maxdif = 0
        for i in range(1, len(prices)):
            if prices[i] < minpri:
                minpri = prices[i]
            elif prices[i] - minpri > maxdif:
                maxdif = prices[i] - minpri
        return maxdif
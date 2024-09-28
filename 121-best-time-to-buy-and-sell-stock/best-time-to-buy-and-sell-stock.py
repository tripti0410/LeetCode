class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 : return 0
        minimum=float('inf')
        maximum=0
        for i in range(0, len(prices)):
            minimum = min(minimum, prices[i])
            cost = prices[i] - minimum
            maximum = max(maximum, cost)
        return maximum
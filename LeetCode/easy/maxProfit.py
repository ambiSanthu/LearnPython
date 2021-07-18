class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = buy
        profit = sell - buy
        for i in prices:
            if i < buy:
                buy = i
                sell = i
            elif i > sell:
                sell = i
            if profit < (sell-buy):
                profit = sell - buy
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 99999999
        profit_price = 0

        for i in prices:
            if i < min_price:
                min_price = i
            current_dif = i - min_price
            if current_dif > profit_price:
                profit_price = current_dif
        
        return profit_price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0
        
        max_profit = 0
        while right <= len(prices) - 1:
            max_profit = max(max_profit, prices[right] - prices[left])
            while prices[right] < prices[left] and left < right:
                left += 1
            right += 1

        return max_profit   
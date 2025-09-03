from typing import List

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1    # We initialize a buy pointer and a sell pointer at positions 0 and 1 as we cannot sell on the same day and because we cannot sell what we don't have
        maxProfit = 0       # At first our max buy price is 0

        while buy < len(prices):    # While the buy pointer is lower than the total length of the array we want to check if we're profitable
            # Profitable?
            if prices[buy] < prices[sell]:              # We are comparing the prices, if we the sell price is higher than the buy price then we calculate the profit
                profit = prices[sell] - prices[buy]     # The profit would be how much we sold - at how much we bought e.g sold at 8, bought at 6 our profit is 2
                maxProfit = max(maxProfit, profit)      # We check what our max profit is, we are comparing the current max Profit (0 at the start) to the profit we just calculated
            else:
                buy = sell  # If the sell price is NOT higher than the buy prices, that means that the buy price is lower which means now is the time to buy
            
            sell += 1       # We move our sell pointer to the right to extend the window
        
        return maxProfit    # Once the loop is finished we return the max profit we can achieve

# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # We initialize our profit at 0
        for i in range(len(prices)):                # Now for every number in the range of prices we want to set it as our buy
            buy = prices[i]
            for j in range(i + 1, len(prices)):     # We will sell at every following number
                sell = prices[j]
                profit = max(profit, sell - buy)    # The profit will be  the maximum between our current profit and our new calculated profit
        return profit   # Once we're done with the loop we will return the profit

# Time complexity: O(n)
# Space complexity: O(1)
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0       # Our starting max profit is 0
        minBuy = prices[0]  # Our minimum buy is the first value

        for sell in prices: # We want to check for every number in the prices if it's worth selling
            maxProfit = max(maxProfit, sell - minBuy)   # Our max profit now become the max between the current max profit and the result of sell and minimum buy
            minBuy = min(minBuy, sell)                  # Now minimum buy becomes the minimum between the minimum buy and the sell price
        
        return maxProfit    # Once we're done looping we return the max profit
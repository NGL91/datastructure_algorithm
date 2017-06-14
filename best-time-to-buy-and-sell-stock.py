# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
#
class Solution():
	def maxProfit(self, lists):
		min_price = float('inf')
		max_profit = 0
		for price in prices:
			min_price = min(min_price, price)
			max_profit = max(max_profit, price-min_price)

		return max_profit





if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print result
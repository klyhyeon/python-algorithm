
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return

# 차이가 가장 큰 경우 (꼭 가장 작고 가장 큰 수일 필요는 없다)
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# 팔 수 없는 경우(마지막날이 가장 낮은 가격)
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# 성공: 21분
#Code Style
# Readability: Excellent
# Structure: Excellent
# Suggestions: Your code is clean, readable, and follows standard conventions perfectly.



from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_num = 10001
        max_num = -1
        for price in prices:
            if price < min_num:
                min_num = price
                max_num = -1
                continue
            if price > max_num:
                max_num = price
            if max_num - min_num > answer:
                answer = max_num - min_num
        return answer

print(Solution().maxProfit([2,1,2,0,1]))

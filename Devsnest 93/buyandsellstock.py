# language used is python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now=10000
        max_profit=0
        for i in prices:
            if min_till_now>i:
                min_till_now=i
            elif max_profit<i-min_till_now:
                 max_profit=i-min_till_now
        return max_profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f, s = 0, 1
        max_diff = 0

        while s <= len(prices) - 1:
            if prices[f] < prices[s]:
                max_diff = max(max_diff, prices[s] - prices[f])
            else:
                f = s
            s += 1


        return max_diff
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_val = prices[0], prices[0]
        answer = 0

        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val, max_val  = prices[i], prices[i]

            max_val = max(max_val, prices[i])
            

            answer = max(answer, max_val - min_val)

        return answer
                
"""
0,1,5,3,7
"""
        
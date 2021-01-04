import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return(0)
        
        max_k = 1
        n = len(prices)
        dp = np.zeros((n, max_k+1, 2), dtype='int').tolist()
        
        for i in range(max_k+1):
            dp[0][i][0] = 0
        
        for i in range(max_k+1):
            dp[0][i][1] = -prices[0]
        
        for i in range(n):
            dp[i][0][1] = -float("Inf")
            
        for i in range(1,n):
            for k in reversed(range(1,max_k+1)):
                
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0] - prices[i])

        return(dp[n-1][max_k][0])
    
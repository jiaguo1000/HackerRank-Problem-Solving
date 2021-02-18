class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return(self.dp(coins, memo, amount))
        
    def dp(self, coins, memo, amount):
        if amount in memo:
            return(memo[amount])
        
        if amount==0:
            return(0)
        if amount<0:
            return(-1)
        
        res = float('INF')
        for coin in coins:
            temp = self.dp(coins, memo, amount-coin)
            if temp==-1:
                continue
            res = min(res, temp+1)
        
        memo[amount] = res if res!=float('INF') else -1
        return(memo[amount])
        
        
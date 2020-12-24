class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return(self.helper(memo, n))
    
    def helper(self, memo, n):
        if n==0:
            memo[n] = 0
        
        if n==1 or n==2:
            memo[n] = 1
            
        if n in memo:
            return(memo[n])
        
        if n not in memo:
            memo[n] = self.helper(memo, n-1)+self.helper(memo, n-2)
            
        return(memo[n])
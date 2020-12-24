class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if len(p)==0:
            return(len(s)==0)
        
        first = s and (p[0]=='.' or p[0]==s[0])
        
        if len(p)>=2 and p[1] == '*':
            res = self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
            return(res)
        else:
            res = first and self.isMatch(s[1:], p[1:])
            return(res)
        
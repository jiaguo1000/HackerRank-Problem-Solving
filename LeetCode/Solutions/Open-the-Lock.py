from collections import deque

class Solution:
    def nextMove(self, s):
        res = []
        for i in range(4):
            for j in [1,-1]:
                temp = list(s)
                temp[i] = int(temp[i])+j
                if temp[i]==10:
                    temp[i] = 0
                if temp[i]==-1:
                    temp[i] = 9
                temp[i] = str(temp[i])
                temp = "".join(temp)
                res.append(temp)
        return(res)
    
    def openLock(self, deadends: List[str], target: str) -> int:
        if ("0000" in deadends) or (target in deadends):
            return(-1)
        
        q = deque(["0000"])
        visited = set(deadends)
        level = deque([0])
        
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                curr_level = level.popleft()
                if curr==target:
                    return(curr_level)

                if curr in visited:
                    continue
                q.extend(self.nextMove(curr))
                visited.add(curr)
                level.extend([curr_level+1]*8)
        
        return(-1)
        
        
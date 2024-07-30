from typing import List
from collections import deque
class Solution:
    def solve(self,m):
        row = len(m)
        col = len(m[0])
        result = []
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        dire = 'UDLR'
        q = deque()
        if m[0][0]==1:
            q.append((0,0,""))
            
        while q:
            i,j,s = q.popleft()
            m[i][j]=0
            if i==row-1 and j==col-1:
                result.append(s)
            for d in range(4):
                i1 = i+direction[d][0]
                i2 = j+direction[d][1]
                if i1>=0 and i1<row and i2>=0 and i2<col and m[i1][i2]==1:
                    q.append((i1,i2,s+dire[d]))
                    
                    
            
        return result
            
    def findPath(self, m: List[List[int]]) -> List[str]:
        r = self.solve(m)
        return r
        

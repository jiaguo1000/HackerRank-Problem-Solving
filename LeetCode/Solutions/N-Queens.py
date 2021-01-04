class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        single_res = []
        board = ["."*n]*n
        
        self.DFS(board, single_res, res)
        return(res)
    
    def isValid(self, board, row, col):
        if row==0:
            return(True)
        
        n = len(board)
        for i in range(row):
            if board[i][col] == 'Q':
                return(False)
        
        i = row-1
        j = col+1
        while i>=0 and j<=n-1:
            if board[i][j] == 'Q':
                return(False)
            i -= 1 
            j += 1
            
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return(False)
            i -= 1 
            j -= 1
        
        return(True)

    
    def DFS(self, board, single_res, res):
        if len(single_res)==len(board):
            res.append(single_res)
            return
        
        row = len(single_res)
        for col in range(len(board)):
            if not self.isValid(board, row, col):
                continue
            
            temp = list(board[row])
            temp[col] = "Q"
            board[row] = "".join(temp)
            self.DFS(board, single_res+[board[row]], res)
            
            temp = list(board[row])
            temp[col] = "."
            board[row] = "".join(temp)
            
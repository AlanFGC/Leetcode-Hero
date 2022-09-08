def backtracking(row, cols, board, n, res):
    if row == n:
        newBoard = [""] * n
        for i in range(n):
            newBoard[i] = ''.join(ch for ch in board[i])
        res.append(newBoard.copy())
        return
    
    for i in range(n):
        if i in cols:
            continue
        
        flag = checkQueen(board, (row, i), n)
        
        if not flag:
            board[row][i] = 'Q'
            cols.add(i)
            backtracking(row + 1, cols, board, n, res)
            cols.remove(i)
            board[row][i] = '.'
    return False


def checkQueen(board, queenPos, n):
    top = queenPos[0] + 1
    bottom = queenPos[0] - 1
    right = queenPos[1] + 1
    left = queenPos[1] - 1
    #check states
    while left >= 0 or right < n  or bottom >= 0 or top < n:
        if arrCheck(top, right, n, board):
            return True
        elif arrCheck(top, left, n, board):
            return True
        elif arrCheck(bottom, right, n, board):
            return True
        elif arrCheck(bottom, left, n, board):
            return True
        top += 1
        bottom -= 1
        right += 1
        left -= 1
    return False
        
        
def arrCheck(x, y, n, board):
    if (x >= n or x < 0) or (y >= n or y < 0):
        return False
    elif board[x][y] == 'Q':
        return True
    else:
        return False
            

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ["." for i in range(n)] for i in range(n)]
        # assume that every row at most can have one queen
        # every column at most can have one queen.
        # we must configure the board in such a way that queens don't attack
        # each other diagonally.
        res = []
        cols = set()
        # generate all possible ways but cut the solution if it doesn't work
        backtracking(0, cols, board, n, res)       
        return res
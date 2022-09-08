def backtracking(row, queens, board, n, res):
    if row == n:
        newBoard = [""] * n
        for i in range(n):
            newBoard[i] = ''.join(ch for ch in board[i])
        res.append(newBoard.copy())
        return
    
    for i in range(n):
        flag = checkQueen(board, queens, (row, i), n)
        if not flag:
            board[row][i] = 'Q'
            queens.add((row, i))
            backtracking(row + 1, queens, board, n, res)
            queens.remove((row, i))
            board[row][i] = '.'
    return False


def checkQueen(board, queens, queenPos, n):
    for oldQueen in queens:
        # remember remember the fifth of november 
        # la diferencia de una diagonal es el valo absoluto de los dos x y de los y
        # si son iguales, entonces están en diagonal
        diffX = abs(oldQueen[0] - queenPos[0])
        diffY = abs(oldQueen[1] - queenPos[1])
        if diffY == diffX or oldQueen[0] == queenPos[0] or oldQueen[1] == queenPos[1]:
            return True
    return False
            

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ["." for i in range(n)] for i in range(n)]
        # assume that every row at most can have one queen
        # every column at most can have one queen.
        # we must configure the board in such a way that queens don't attack
        # each other diagonally.
        res = []
        queens = set()
        # generate all possible ways but cut the solution if it doesn't work
        backtracking(0, queens, board, n, res)       
        return res
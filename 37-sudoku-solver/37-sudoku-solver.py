# define the id of a box
# there is a faster arithmetic equation, but I don't really get it:
# box_id = (i // 3) * 3 + j // 3
def getBoxId(i, j):
    if i < 3:
        if j < 3:
            return 0
        elif j >= 3 and j < 6:
            return 1
        elif j >= 6:
            return 2
    elif i >= 3 and i < 6:
        if j < 3:
            return 3
        elif j >= 3 and j < 6:
            return 4
        elif j >= 6:
            return 5
    elif i >= 6:
        if j < 3:
            return 6
        elif j >= 3 and j < 6:
            return 7
        elif j >= 6:
            return 8
    return None




def backTrack(x, y, rows, cols, boxes, board):
    if x >= 8 and y >= 8:
        return True
    # we advance one step here:
    i = x + ((y+1) // 9)
    j = y + 1
    j = j % 9
    
    if x == 0 and y == 0 and board[x][y] == '.':
        i = 0
        j = 0
    elif board[i][j] != '.':
        if backTrack(i, j, rows, cols, boxes, board):
            return True
        else:
            return False
    
    boxId = getBoxId(i, j)
    for k in range(1, 10):
        if k not in rows[i] and k not in cols[j] and k not in boxes[boxId] :
            rows[i].add(k)
            cols[j].add(k)
            boxes[boxId].add(k)
            board[i][j] = str(k)
            if backTrack(i, j, rows, cols, boxes, board):
                return True
            
            rows[i].remove(k)
            cols[j].remove(k)
            boxes[boxId].remove(k)
            board[i][j] = '.'
            
    return False
                
        

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we are using sets to aid us in the back tracking
        # sets for cols, sets for rows and sets for boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    value = board[i][j]
                    rows[i].add(int(value))
                    cols[j].add(int(value))
                    boxes[getBoxId(i, j)].add(int(value))

        # backtracking steps
        backTrack(0, 0, rows, cols, boxes, board)
 
        return None
        
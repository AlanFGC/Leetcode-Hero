class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search to find row,
        lenRows = len(matrix)
        
        low = 0
        high = lenRows-1
        
        while low<=high:
            m = (high+low) // 2 
            if matrix[m][0] > target:
                if (m - 1) >= 0 and matrix[m - 1][0] < target:
                    m = m - 1
                    break
                else:
                    high = m - 1
            elif matrix[m][0] < target:
                if (m + 1) < lenRows and matrix[m + 1][0] > target:
                    m = m
                    break
                else:
                    low = m + 1
            else:
                return True
        
        row = m
        print(row)
        low = 0
        lenCol = len(matrix[0])
        high = lenCol - 1
        
        while low<=high:
            mid = (high+low)// 2
            print(matrix[row][mid])
            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True
    
        return False
        
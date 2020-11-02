from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """Return (clockwise) spiral order of input matrix."""
        
    if not matrix:
        return []
            
    def tracePath(m, n, offsetRow = 0, offsetCol = 0):
        """Return spiral order assuming m rows and n columns,
        with corresponding offsetRow rows and offsetCol cols."""

        if m < 1 or n < 1:
            return []
        
        if m == 1:
            return matrix[offsetRow][offsetCol:(offsetCol + n)]

        if n == 1:
            return [matrix[row][offsetCol]
                    for row in range(offsetRow, offsetRow + m)]
            
        res = []
        # Top-left to top-right
        for col in range(offsetCol, offsetCol + n - 1):
            res.append(matrix[offsetRow][col])
        
        # Top-right to bottom-right
        for row in range(offsetRow, offsetRow + m - 1):
            res.append(matrix[row][offsetCol + n - 1])
        
        # Bottom-right to bottom-left
        for col in range(offsetCol + n - 1, offsetCol, -1):
            res.append(matrix[offsetRow + m - 1][col])
            
        # Bottom-left to top-left
        for row in range(offsetRow + m - 1, offsetRow, -1):
            res.append(matrix[row][offsetCol])
        
        return res + tracePath(m - 2, n - 2, offsetRow + 1, offsetCol + 1)
    
    m, n = len(matrix), len(matrix[0])
    return tracePath(m, n)
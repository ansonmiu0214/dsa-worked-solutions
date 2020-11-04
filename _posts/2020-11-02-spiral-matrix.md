---
title: Spiral matrix
date: 2020-11-02
shortname: spiral_matrix
leetcode: https://leetcode.com/problems/spiral-matrix
tags: [matrix]
---

## Problem
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

__Example 1:__
```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

## Some questions to ask
* Is m==0 or n==0 valid input?

## Approach
Decompose the problem: the sprial order of a m-by-n matrix is the 'outer spiral' followed by the
spiral order of the inner (m-1)-by-(n-1) matrix.

We can generalise further by keeping track of the row offset (`offsetRow`) and column offset (`offsetCol`), 
both initially set to 0 -- 
the (m, n) spiral order is its outer spiral followed by the (m-1, n-1) spiral order with row offset `offsetRow + 1` and
column offset `offsetCol + 1`.

For the base cases:
* (1, _) spiral order is a single row, where we just print the elements in order
* (_, 1) spiral order is a single column, where we just print the elements from top to bottom
* (0, \_) and (_, 0) do not cover any elements

```python
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
```

### Complexity
Let the input matrix have m rows and n columns

* O(mn) time complexity from iterating over the whole matrix
* O(mn) space complexity with the return value
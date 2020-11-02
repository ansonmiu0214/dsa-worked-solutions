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
* (0, \_) and (_ do not cover any elements

```python3

```


### Complexity

### Other approaches

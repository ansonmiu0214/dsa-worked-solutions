---
title: Valid square
date: 2020-11-11
shortname: valid_square
leetcode: https://leetcode.com/problems/valid-square
tags: [math]
---

## Problem

> Given the coordinates of four points in 2D space, return whether 
> the four points could construct a square.
> 
> The coordinate `(x,y)` of a point is represented by an integer
> array > with two integers.
>
> __Example:__
>
> ```
> Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
> Output: True
> ```

## Some questions to ask

* What about a square of area 0?
* Are the input points ordered?

## Approach

Side length equality is a necessary but insufficient criterion for
validating a square, because this applies to rhombuses too.

However, unlike rhombuses, squares also have diagonal length equality too, so this can be used as a discriminator.

We can find all side lengths and diagonal lengths by computing the
distance between all pairs of points. Squares will have two unique
lengths, whilst rhombuses will have three unique lengths.

The Vector class encapsulates the vector operations such as
computing L2-norm, and overloads operators for arithmetic operations.

```python
class Vector:

    def __init__(self, *entries):
        self._entries = entries

    @property
    def entries(self):
        return self._entries

    @property
    def l2(self):
        return sqrt(sum(v_i ** 2 for v_i in self.entries))

    def __sub__(self, other):
        """Perform vector subtraction."""

        return Vector(*[u_i - v_i
                        for u_i, v_i in zip(self.entries, other.entries)])

    def __mul__(self, other):
        """Perform vector dot product."""

        return sum(u_i * v_i for u_i, v_i in zip(self.entries, other.entries))

    def __repr__(self):
        return f'Vector({",".join(map(str, self.entries))})'

    def __str__(self):
        return f'({",".join(map(str, self.entries))})'

def validSquare(p1: List[int],
                p2: List[int],
                p3: List[int],
                p4: List[int]) -> bool:
    """Return whether (p1, p2, p3, p4) are vertices of a valid square."""

    points = [Vector(*p1),
              Vector(*p2),
              Vector(*p3),
              Vector(*p4),]

    # Get lengths between all points: a square should have equal, non-zero
    # side lengths and equal diagonals (greater than side lengths).
    seenLengths = set((u - v).l2
                      for i, u in enumerate(points)
                      for j, v in enumerate(points)
                      if i != j)

    return len(seenLengths) == 2 and min(seenLengths) > 0
```

### Complexity
The 'input size' doesn't vary for this problem, so it runs in
constant time and space complexity.

Of course, the magnitude of the coordinates can vary, but it does
not affect the asymptotic running time of the solution.

### Other approaches
Another way of validating the vertices of a square is to
check that the cosine of each interior angle is 0, in addition
to all side lengths being the same
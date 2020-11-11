from math import sqrt
from typing import List
from itertools import combinations

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
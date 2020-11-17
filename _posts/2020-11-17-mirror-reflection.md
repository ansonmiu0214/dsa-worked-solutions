---
title: Mirror reflection
date: 2020-11-17
shortname: mirror_reflection
leetcode: https://leetcode.com/problems/mirror-reflection
tags: [monthly challenge, simulation]
---

## Problem

> There is a special square room with mirrors on each of the four walls.
> Except for the southwest corner, there are receptors on each of the remaining corners, numbered `0`, `1`, and `2`.
> 
> The square room has walls of length `p`, and a laser ray from the southwest corner first meets the east wall 
> at a distance `q` from the `0`th receptor.
> 
> Return the number of the receptor that the ray meets first.
> (It is guaranteed that the ray will meet a receptor eventually.)

## Approach

Simulate the movement of the ray.
Calculate the time when the ray next hits a wall, and keep track of its position. Depending on which wall the ray hits, reflect the direction vector accordingly.

```python
def mirrorReflection(p: int, q: int) -> int:
    """Return the number of the receptor that the ray meets first, given
    the starting position of (0, 0) in a 'p-sided square room with the ray
    first meting the east wall at distance 'q' from the 0th receptor."""

    x, y = 0, 0
    dx, dy = p, q

    corners = set([0, p])
    pointToReceptors = {point: idx
                        for idx, point in enumerate([(p, 0), (p, p), (0, p)])} 

    while (x, y) not in pointToReceptors:
        # Let (x', y') denote next position after 'time'.
        # (x', y') = (x + dx * time, y + dy * time)

        # Find possible times of hitting each wall, but pick the
        # most recent (non-negative) time as 'next'.
        possibleTimes = [F(-x, dx), F(p-x, dx),     # time when x' = 0 or p
                         F(-y, dy), F(p-y, dy)]     # time when y' = 0 or p
        nextTime = min([time for time in possibleTimes if time > 0])

        x += dx * nextTime
        y += dy * nextTime

        # Reflect direction if hit wall.
        if x in corners:
            dx *= -1
        if y in corners:
            dy *= -1
        
    return pointToReceptors[(x, y)]
```

### Complexity
* O(p) time complexity, as the simulation is bounded by the size of the room
* O(1) space complexity, from keeping track of the current position and direction
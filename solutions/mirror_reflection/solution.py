from fractions import Fraction as F

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
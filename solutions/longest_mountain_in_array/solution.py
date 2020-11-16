from typing import List

def longestMountain(arr: List[int]) -> int:
    """Return length of longest mountain in array."""

    UNKNOWN = 0
    UP = 1
    DOWN = 2

    longestLength = 0

    # Keep track of current mountain length, whether a mountain
    # is found at the current iteration, and the current direction.
    currLength = 0

    # We don't know the initial slope.
    direction = UNKNOWN

    first, *rest = arr
    prev = first

    for curr in rest:
        if direction == UNKNOWN:
            if prev < curr:
                # Both 'prev' and 'curr' contribute to upward slope.
                currLength = 2
                direction = UP

        elif direction == UP:
            if prev < curr:
                currLength += 1
            elif prev > curr:
                # 'curr' contributes to downward slope.
                currLength += 1
                direction = DOWN
            else:
                # Flat ground reached, so we reset the current state.
                direction = UNKNOWN
                currLength = 0

        else:
            if prev > curr:
                currLength += 1
            else:
                # Bottom of mountain reached, update global maximum.
                longestLength = max(longestLength, currLength)

                if prev < curr:
                    currLength = 2
                    direction = UP
                else:
                    currLength = 0
                    direction = UNKNOWN

        prev = curr

    # If we end with a downward slope, it is possible that the length
    # of the current mountain is the global maximum.
    return max(longestLength, currLength) if direction == DOWN else longestLength
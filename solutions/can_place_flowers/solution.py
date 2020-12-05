from typing import List

def canPlaceFlowers(flowerBed: List[int], n: int) -> bool:
    """Return true iff 'n' new flowers can be added to the 'flowerBed'."""

    length = len(flowerBed)

    # Memoise results from 'maximumNewFlowers' function.
    cache = {}

    def maximumNewFlowers(index: int = 0):
        """Return maximum number of new flowers that can be placed in the
        'flowerBed', starting at the specified 'index'."""

        if index in cache:
            return cache[index]

        if index >= length:
            # Out of bounds.
            cache[index] = 0
        
        elif index + 1 == length:
            # Place flower here if current position is empty.
            cache[index] = 1 - flowerBed[index]

        elif flowerBed[index] == 1:
            # Current position is not empty.
            cache[index] = maximumNewFlowers(index + 2)

        elif flowerBed[index + 1] == 0:
            # Next position is empty -- place flower here.
            cache[index] = 1 + maximumNewFlowers(index + 2)

        else:
            # Next position is not empty.
            cache[index] = maximumNewFlowers(index + 1)

        return cache[index]

    return n <= maximumNewFlowers()

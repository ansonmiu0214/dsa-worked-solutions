from string import ascii_lowercase

def getSmallestString(n: int, k: int) -> str:
    """Return lexiographically smamllest (lower-case) string with
    length equal to 'n' and numeric value equal to 'k'."""

    alphabetSize = len(ascii_lowercase)

    # Start with most optimal string (i.e. all 'a's) and
    # build up from the 'least significant character', i.e. RHS.
    optimalValues = [1] * n

    # Distribute leftover characters from least significant side.
    end = n - 1
    leftover = k - n
    
    while leftover > 0:
        # Value max out at 'alphabetSize', propagate rest to leftover.
        toAdd = min(alphabetSize - optimalValues[end], leftover)
        optimalValues[end] += toAdd
        leftover -= toAdd
        end -= 1

    # Require 'index - 1' to convert 1-index values to 0-index for list.
    return ''.join(ascii_lowercase[index - 1] 
                   for index in optimalValues)
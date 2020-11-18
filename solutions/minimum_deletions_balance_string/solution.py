def minimumDeletions(s: str) -> int:
    """Return minimum number of deletions to make 's' balanced, i.e. 
    no 'b' comes before 'a' in string consisting of just 'a's and 'b's."""

    deletions = 0
    countOfBs = 0
    for c in s:
        if c == 'a' and countOfBs > 0:
            # Only need to delete 'b' if it comes before an 'a'.
            countOfBs -= 1
            deletions += 1
        elif c == 'b':
            # Keep track of number of 'b's seen.
            countOfBs += 1
    return deletions

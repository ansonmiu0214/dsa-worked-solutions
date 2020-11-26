from collections import Counter

def longestSubstring(s: str, k: int) -> int:
    """Return the length of the longest substring in 's' such that the
    frequency of each character in this substring is at least 'k'."""

    if len(s) < k:
        # String shorter than k characters cannot possibly have a 
        # substring with characters repeated at least k times.
        return 0

    numUniqueChars = len(set(s))
    longestLength = 0

    for targetCount in range(1, numUniqueChars + 1):
        # Focus on substrings with 'targetCount' number of unique
        # characters that each repeat at least k times.

        counter = Counter()
        countUniqueChars = 0

        numCharsOccurKTimes = 0
        start = end = 0

        while end < len(s):

            if countUniqueChars <= targetCount:
                # Extend window to either find more unique chars, or
                # find a longer substring that matches the criteria.

                if counter[s[end]] == 0:
                    countUniqueChars += 1
                
                counter[s[end]] += 1

                if counter[s[end]] == k:
                    numCharsOccurKTimes += 1
                
                end += 1

            else:
                # Shrink window to reduce number of unique chars.

                if counter[s[start]] == k:
                    numCharsOccurKTimes -= 1
                
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    countUniqueChars -= 1
                
                start += 1

            if countUniqueChars == targetCount == numCharsOccurKTimes:
                # Found a candidate substring s[start:end] which has 'targetCount'
                # unique characters, each occurring at least k times.
                longestLength = max(longestLength, end  - start)

    return longestLength
def decodeString(s: str) -> str:
    """Return decoded string, given encoded string 's'."""
    
    def decodeScope(i: int = 0, repeat: int = 1):
        """Decode the encoding scope beginning at index 'i', given the
        enclosing number of 'repeat's. Returns a tuple of the next index
        to process along with the decoded string for this scope."""

        decoded = []
        while i < len(s):
            if s[i].isdigit():
                # Found 'k[encoded_string]'.
                #        ^
                # Parse numerical value for the repeat of the inner scope.
                nextRepeat = 0
                while s[i] != '[':
                    nextRepeat *= 10
                    nextRepeat += int(s[i])
                    i += 1
                
                # Found 'k[encoded_string]', parsed 'k' as 'nextRepeat'.
                #         ^
                # Inner scope begins at index 'i + 1'.
                i, innerDecoded = decodeScope(i + 1, nextRepeat)
                decoded += innerDecoded
            elif s[i] == ']':
                i += 1
                break
            else:
                decoded.append(s[i])
                i += 1

        return i, (decoded * repeat)

    _, decoded = decodeScope()
    return ''.join(decoded)
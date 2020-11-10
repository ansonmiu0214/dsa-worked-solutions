from collections import Counter

class FreqStack:

    def __init__(self):
        self._itemToFreq = Counter()
        self._freqStack = [[]]

    def push(self, x: int) -> None:
        """Push integer 'x' onto the stack."""

        # Update item frequency.
        newFreq = self._itemToFreq[x] + 1
        self._itemToFreq[x] = newFreq

        # Push item into frequency stack corresponding
        # to new frequency, create if necessary.
        if newFreq == len(self._freqStack):
            self._freqStack.append([x])
        else:
            self._freqStack[newFreq].append(x)

    def pop(self) -> int:
        """Removes and returns the most frequent element. If
        there is a tie, the most recent element is returned."""

        # Remove item from stack with highest frequency.
        item = self._freqStack[-1].pop()
        self._itemToFreq[item] -= 1

        # Remove frequency stack if empty.
        if len(self._freqStack[-1]) == 0:
            self._freqStack.pop()

        return item
class MinStack:

    def __init__(self):

        # Keep track of current min in separate stack.
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        """Push element 'x' onto stack."""

        self._data.append(x)

        # Update current min by comparing 'x' with previous min.
        # If stack was empty, then current min is 'x'.
        currMin = min(self._min[-1], x) if self._min else x
        self._min.append(currMin)
    
    def pop(self) -> None:
        """Removes the element on top of the stack."""

        # Sync state of 'data' stack and 'min' stack.
        self._data.pop()
        self._min.pop()

    def top(self) -> int:
        """Get the top element."""

        return self._data[-1]
    
    def getMin(self) -> int:
        """Retrive the minimum element in the stack."""
        
        return self._min[-1]
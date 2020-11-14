from collections import deque
from ..utils import TreeNode

def isEvenOddTree(root: TreeNode) -> bool:
    """Return true iff tree rooted at 'root' is even-odd tree."""

    if root is None:
        return True
    
    checkNodeForParity = [
        lambda x: x % 2 != 0,   # Even-index nodes must be odd.
        lambda x: x % 2 == 0,   # Odd-index nodes must be even.
    ]

    checkPrevForParity = [
        lambda prev, curr: prev < curr, # Even-index lvl increases (->)
        lambda prev, curr: curr < prev, # Odd-index lvl decreases (<-)
    ]

    prev = None
    prevParity = None

    # Check for conditions using BFS, keeping track of level parity.
    queue = deque([(root, 0)])
    while queue:
        currNode, parity = queue.popleft()
        curr = currNode.val

        if not checkNodeForParity[parity](curr):
            return False

        if prevParity == parity:
            if not checkPrevForParity[parity](prev, curr):
                return False
    
        prev = curr
        prevParity = parity

        if currNode.left is not None:
            queue.append((currNode.left, 1 - parity))
    
        if currNode.right is not None:
            queue.append((currNode.right, 1 - parity))
    
    return True
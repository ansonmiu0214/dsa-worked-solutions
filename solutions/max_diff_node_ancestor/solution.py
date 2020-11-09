from typing import Optional
from ..utils import TreeNode

def maxAncestorDiff(node: TreeNode,
                    maxAncestor: Optional[int] = None,
                    minAncestor: Optional[int] = None) -> int:
    """Return maximum difference between any node rooted in
    `tree` and its ancestors, given the encountered
    `maxAncestor` and `minAncestor`."""

    if node is None:
        return 0

    if maxAncestor is not None and minAncestor is not None:
        # Compute maximum ancestor difference
        # for current node w.r.t. its ancestors
        currDiff = max(abs(node.val - maxAncestor),
                       abs(node.val - minAncestor))
    else:
        currDiff = 0
    
    # Update (max|min) ancestors for children
    if maxAncestor is None or node.val > maxAncestor:
        maxAncestor = node.val
    
    if minAncestor is None or node.val < minAncestor:
        minAncestor = node.val
    
    maxDiffLeftChild = maxAncestorDiff(node.left,
                                       maxAncestor,
                                       minAncestor)
    maxDiffRightChild = maxAncestorDiff(node.right,
                                        maxAncestor,
                                        minAncestor)

    # Reduce maximum ancestor difference 
    # as found from children
    return max(currDiff, maxDiffLeftChild, maxDiffRightChild)
from collections import deque
from ..utils import TreeNode

def lcaDeepestLeaves(root: TreeNode) -> TreeNode:
    """Given the 'root' of a binary tree, return the 
    lowest common ancestor of its deepest leaves."""

    if not root.left and not root.right:
        # Base case, if the root is itself a leaf.
        return root

    deepestLeaves = []
    deepestLevel = 0

    parentOf = {}
    nodeOf = {}

    # Apply BFS and keep track of deepest leaves.
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()

        # Keep track of val -> node mapping, as we return a 'TreeNode'.
        nodeOf[node.val] = node
    
        if node.left or node.right:
            if node.left:
                parentOf[node.left.val] = node.val
                queue.append((node.left, level + 1))
            if node.right:
                parentOf[node.right.val] = node.val
                queue.append((node.right, level + 1))
        else:
            # Found possible deepest leaf candidate.
            # Update 'deepestLevel' if this node is deepest.

            if level > deepestLevel:
                deepestLevel = level
                deepestLeaves = []

            deepestLeaves.append(node.val)
    
    # Map deepest leaves to their parents until they share the same
    # parent -- the set will discard duplicate parents.
    lowestCommonAncestors = set(deepestLeaves)
    while len(lowestCommonAncestors) > 1:
        lowestCommonAncestors = set(parentOf[node]
                                    for node in lowestCommonAncestors)

    lowestCommonAncestor = next(iter(lowestCommonAncestors))
    return nodeOf[lowestCommonAncestor]
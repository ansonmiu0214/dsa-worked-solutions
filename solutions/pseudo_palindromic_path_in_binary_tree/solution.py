from ..utils import TreeNode

def pseudoPalindromicPaths (root: TreeNode) -> int:
    """Return number of pseudo-palindromic paths in tree rooted at `root`."""

    nodesWithOddOccurrences = set()

    def flip(val: int):
        """Flip membership of `val` in `nodesWithOddOccurrences`."""
        if val in nodesWithOddOccurrences:
            nodesWithOddOccurrences.remove(val)
        else:
            nodesWithOddOccurrences.add(val)

    def countPathsFromDFS(node: TreeNode, pathSoFar: int = 0):
        if node is None:
            return 0
        
        # Increment count of `node.val` in "visited"
        flip(node.val)
        pathSoFar += 1
        if node.left is None and node.right is None:
            # For even-length paths, all values must have even-parity occurrences to be palindrome.
            # For odd-length paths, exactly one value must have odd-parity occurrence.
            count = int(pathSoFar % 2 == len(nodesWithOddOccurrences))
        else:
            count = countPathsFromDFS(node.left, pathSoFar) + countPathsFromDFS(node.right, pathSoFar)
        
        # Decrement count of `node.val` in "visited"
        flip(node.val)
        return count
    
    return countPathsFromDFS(root)
from typing import Tuple
from ..utils import TreeNode

def transformIntoSortedList(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
    """Transform binary search tree rooted at the specified 'node' into a
    linked list. Return the head and tail of the linked list.""" 

    if node.left is not None:
        # Transform left child into linked list, and connect the *tail*
        # of that linked list to the current node.
        head, leftTail = transformIntoSortedList(node.left)
        node.left = None
        leftTail.right = node
    else:
        head = node

    if node.right is not None:
        # Transform right child into linked list, and connect the current
        # node to the *head* of that linked list.
        mid, tail = transformIntoSortedList(node.right)
        node.right = mid
    else:
        tail = node

    return head, tail


def increasingBST(root: TreeNode) -> TreeNode:
    """Return linked list representation of the specified 'root' BST."""

    head, _ = transformIntoSortedList(root)
    return head

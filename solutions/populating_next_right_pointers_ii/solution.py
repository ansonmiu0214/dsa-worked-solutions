from collections import deque

from ..utils import TreeNode

class TreeNodeWithNext(TreeNode):

    def __init__(self, val, left=None, right=None, next=None):
        super().__init__(val, left, right)
        self.next = next

    def toList(self):

        leftMostNodes = []
        currLvl = -1
        queue = deque([(self, 0)])
        while queue:
            node, lvl = queue.popleft()
            if lvl > currLvl:
                leftMostNodes.append(node)
                currLvl = lvl

            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))

        NULL_PLACEHOLDER = '#'
        nodes = []
        for leftMostNode in leftMostNodes:
            curr = leftMostNode
            while curr is not None:
                nodes.append(curr.val)
                curr = curr.next
            nodes.append(NULL_PLACEHOLDER)
        return nodes

def connect(root: TreeNodeWithNext) -> TreeNodeWithNext:
    """Populate the 'next' pointer of each node in the tree 
    specified by 'root'."""

    if root is None:
        return root

    currParent = root
    while currParent is not None:
        # Connect the nodes in the level below 'currParent', i.e.
        # the level where the children of 'currParent' resides.

        prevNode = None
        nextParent = None
        while currParent is not None:

            # Iterate through children nodes and connect their
            # right pointers.
            for child in (currParent.left, currParent.right):
                if child is None:
                    continue

                # Connect 'next' pointer of 'prevNode' if possible,
                # and update 'prevNode'.
                if prevNode is not None:
                    prevNode.next = child

                prevNode = child
                if nextParent is None:
                    # Found the leftmost node in the next level.
                    nextParent = child
            
            # Go across to next node in the same level.
            currParent = currParent.next
        
        # Set 'currParent' to be the leftmost node in the next level.
        currParent = nextParent

    return root
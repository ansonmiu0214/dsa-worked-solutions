from collections import deque
from unittest.main import main

class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromList(cls, list):
        if len(list) == 0:
            return None

        first, *rest = list
        if first is None:
            raise Exception('Root node cannot be null')

        root = cls(first)

        LEFT_CHILD = 0
        RIGHT_CHILD = 1

        curr = root
        mode = LEFT_CHILD
        queue = deque()

        for val in rest:
            if val is not None:
                node = cls(val)
                queue.append(node)
            else:
                node = None

            if mode == LEFT_CHILD:
                curr.left = node
            elif mode == RIGHT_CHILD:
                curr.right = node
                curr = queue.popleft()
                
            mode = 1 - mode
        
        return root

    def toList(self):
        result = [self.val]
        queue = deque([self])

        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
                result.append(node.left.val)
            else:
                result.append(None)
            
            if node.right is not None:
                queue.append(node.right)
                result.append(node.right.val)
            else:
                result.append(None)

        while result[-1] is None:
            result.pop()
        
        return result
from .solution import isEvenOddTree
from ..utils import TreeNode

print('Enter tree, e.g. [2,3,1,3,1,null,1]:', end=' ')
nodes = [int(node) if node != 'null' else None for node in input().strip().split(',')]

root = TreeNode.fromList(nodes)
evenOddTree = isEvenOddTree(root)
print('The Tree is Even-Odd' if evenOddTree else 'The Tree is NOT Even-Odd')
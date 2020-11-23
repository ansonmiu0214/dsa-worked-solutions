from .solution import rob
from ..utils import TreeNode

print('Enter tree, e.g. [2,3,1,3,1,null,1]:', end=' ')
nodes = [int(node) if node != 'null' else None for node in input().strip().split(',')]

root = TreeNode.fromList(nodes)
amount = rob(root)
print(f'Max amount from rob: ${amount}')
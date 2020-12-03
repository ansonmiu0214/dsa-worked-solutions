from solutions.utils.binary_tree import TreeNode
from .solution import increasingBST
from ..utils import io

print('Enter tree, e.g. 2,3,1,3,1,null,1:', end=' ')
nodes = [int(node) if node != 'null' else None
         for node in io.get_list(str)]

root = TreeNode.fromList(nodes)

linkedList = increasingBST(root)
print(linkedList.toList())
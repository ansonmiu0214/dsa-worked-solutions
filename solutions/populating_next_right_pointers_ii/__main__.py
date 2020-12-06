from .solution import connect, TreeNodeWithNext
from ..utils import io

print('Enter tree, e.g. 2,3,1,3,1,null,1:', end=' ')
nodes = [int(node) if node != 'null' else None for node in io.get_list(str, delimiter=',')]

tree = TreeNodeWithNext.fromList(nodes)

connected = connect(tree)
print(connected.toList())


from .solution import spiralOrder
from ..utils import io

print('Enter space-separated rows, each row as comma-separated numbers:')

matrix = [[int(entry.strip()) for entry in row.split(',')]
          for row in io.get_list(str)]

transformed = spiralOrder(matrix)

for row in transformed:
    print(' '.join(map(str, row)))
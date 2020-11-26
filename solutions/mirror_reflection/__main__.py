from .solution import mirrorReflection
from ..utils import io

print('Enter space-separated numbers for p and q:', end=' ')
p, q = io.get_list(int)

receptor = mirrorReflection(p, q)
print(f'Ray first hits receptor #{receptor}')
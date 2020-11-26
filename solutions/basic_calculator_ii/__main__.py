from .solution import calculate
from ..utils import io

print('Enter expression:', end=' ')
expr = io.get(str)

answer = calculate(expr)
print(f'{expr} = {answer}')
from .solution import decodeString
from ..utils import io

print('Enter encoded string (rule := k[encoded_string]):', end=' ')
s = io.get(str)

decoded = decodeString(s)
print(f'Decoded string: {decoded}')
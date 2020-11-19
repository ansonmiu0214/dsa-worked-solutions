from .solution import decodeString

print('Enter encoded string (rule := k[encoded_string]):', end=' ')
s = input().strip()

decoded = decodeString(s)
print(f'Decoded string: {decoded}')
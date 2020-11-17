from .solution import mirrorReflection

print('Enter space-separated numbers for p and q:', end=' ')
p, q = list(map(int, input().strip().split(' ')))

receptor = mirrorReflection(p, q)
print(f'Ray first hits receptor #{receptor}')
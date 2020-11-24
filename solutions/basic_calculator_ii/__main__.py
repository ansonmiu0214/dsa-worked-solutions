from .solution import calculate

print('Enter expression:', end=' ')
expr = input().strip()

answer = calculate(expr)
print(f'{expr} = {answer}')
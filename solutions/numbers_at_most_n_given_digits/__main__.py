from solutions.utils.printer import pluralise
from .solution import atMostNGivenDigitSet
from ..utils import printer

print('Enter space-separated digits:', end=' ')
digits = list(map(int, input().strip().split(' ')))

assert all(0 < digit <= 9 for digit in digits), \
    f'Invalid input: {", ".join(map(str, (digit for digit in digits if not 0 < digit <= 9)))}'

print('Enter n:', end=' ')
n = int(input().strip())

possibilities = atMostNGivenDigitSet(digits, n)

print(printer.pluralise(possibility=possibilities))
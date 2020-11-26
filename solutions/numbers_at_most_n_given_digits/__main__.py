from .solution import atMostNGivenDigitSet
from ..utils import io, printer

print('Enter space-separated digits:', end=' ')
digits = io.get_list(int)

assert all(0 < digit <= 9 for digit in digits), \
    f'Invalid input: {", ".join(map(str, (digit for digit in digits if not 0 < digit <= 9)))}'

print('Enter n:', end=' ')
n = io.get(int)

possibilities = atMostNGivenDigitSet(digits, n)

print(printer.pluralise(possibility=possibilities))
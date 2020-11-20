from .solution import minimumDeletions
from ..utils import printer

print('Enter string only consisting of "a"s and "b"s:', end=' ')
s = input().strip().lower()

violating_characters = set(s) - set('ab')
assert len(violating_characters) == 0, f'Violating characters: {", ".join(violating_characters)}'

deletions = minimumDeletions(s)
print(f'Need at least {printer.pluralise(deletion=deletions)} to make "{s}" balanced.')
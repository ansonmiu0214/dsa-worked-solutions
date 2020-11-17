"""Interactive prompt for exploring solution to a particular problem."""

import os
from pathlib import Path
import subprocess

def banner(text: str, *, borderChar: str = '='):
    """Print 'text' as banner, optionally customise 'borderChar'."""

    border = borderChar * len(text)
    return '\n'.join([border, text, border])

# Find solutions (as subpackages), ignoring 'utils'.
current_dir = os.path.dirname(__file__)
packages = sorted([entry for entry in os.listdir(current_dir)
                   if os.path.isdir(os.path.join(current_dir, entry)) \
                       and entry != 'utils' \
                        and not entry.startswith('__')])

longestTitle = max(len(entry) for entry in packages)

# Print legend table.
print(f'----|-{"-" * longestTitle}')
print('Key | Title')
print(f'----|-{"-" * longestTitle}')
for key, package in enumerate(packages):
    print(f'{str(key).rjust(3)} | {package}')
print(f'----|-{"-" * longestTitle}')

# Run interactive prompt.
print()
key = None
while key is None or not 0 <= key < len(packages):
    stdin = input('Select solution by key: ').strip()
    try:
        key = int(stdin)
    except ValueError:
        continue

print()
print(banner(packages[key]))

# Run solution.
parent_dir = Path(current_dir).parent
command = f'cd {parent_dir} && python3 -m solutions.{packages[key]}'
subprocess.run(command, shell=True)
from argparse import ArgumentParser
from datetime import date
import os
from pathlib import Path
import re
import sys

def generateMD(title, today, shortname):
    return '\n'.join((
        '---',
        f'title: {toTitle(title)}',
        f'date: {today}',
        f'shortname: {shortname}',
        f'leetcode: https://leetcode.com/problems/{title}',
        'tags: []',
        '---\n',
        '## Problem\n',
        '## Some questions to ask\n',
        '## Approach\n',
        '### Complexity\n',
        '### Other approaches\n'
    ))

def toTitle(title):
    words = title.split('-')
    words[0] = words[0].title()
    return ' '.join(words)

def main(args):
    parser = ArgumentParser()
    parser.add_argument('title',
                        help='Page title')
    parser.add_argument('shortname',
                        help='Shortname for solutions directory')

    args = parser.parse_args()
    title = args.title
    shortname = args.shortname

    # Validate title and shortname
    pattern = re.compile('^[a-z-]+$')
    if not pattern.match(title):
        print('Title is not well-formed', file=sys.stderr)
        return 1

    pattern = re.compile('^[a-z_]+$')
    if not pattern.match(shortname):
        print('Shortname is not well-formed', file=sys.stderr)
        return 1    

    today = date.today().strftime('%Y-%m-%d')

    post_filename = os.path.join('_posts', f'{today}_{title}.md') 
    solutions_dir = os.path.join('solutions', shortname)

    if os.path.exists(post_filename):
        print('Explanation already exists', file=sys.stderr)
        return 1

    if os.path.exists(solutions_dir):
        print('Solution already exists', file=sys.stderr)
        return 1

    # Write post template
    with open(post_filename, 'w') as f:
        f.write(generateMD(title, today, shortname))

    # Create files
    os.makedirs(solutions_dir)
    Path(os.path.join(solutions_dir, '__init__.py')).touch()
    Path(os.path.join(solutions_dir, '__main__.py')).touch()
    Path(os.path.join(solutions_dir, 'solution.py')).touch()
    Path(os.path.join(solutions_dir, 'test.py')).touch()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
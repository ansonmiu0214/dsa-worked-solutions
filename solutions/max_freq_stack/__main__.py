from .solution import FreqStack
from ..utils import proxyCall

stack = FreqStack()
while True:
    print('> Enter <command> <arg1> <arg2> ... <argn>, or q to quit')
    stdin = input().strip()
    if stdin.lower() == 'q':
        break

    command, *args = stdin.split(' ')
    args = list(map(int, args))

    ret = proxyCall(stack, command, args)
    print(ret)
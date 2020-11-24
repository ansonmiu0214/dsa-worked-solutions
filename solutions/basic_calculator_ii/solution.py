def calculate(expr: str) -> int:
    """Evaluate 'expr', which contains only non-negative integers,
    {+,-,*,/} operators and empty spaces."""

    plusOrMinus = {'+': lambda x, y: x + y ,
                   '-': lambda x, y: x - y}
    mulOrDiv = {'*': lambda x, y: x * y ,
                '/': lambda x, y: x // y}
                
    stack = []
    operators = []
    number = 0

    for char in expr:
        if char.strip() == '':
            # Skip whitespace.
            continue

        if char.isdigit():
            # Add digit to current number.
            number = number * 10 + int(char)
            continue
    
        stack.append(number)
        number = 0

        if operators and operators[-1] in mulOrDiv:
            # Perform multiplication or division first.
            snd = stack.pop()
            fst = stack.pop()
            operator = operators.pop()

            stack.append(mulOrDiv[operator](fst, snd))
        
        operators.append(char)
    
    # The last operand must be a number, so add that to the stack.
    # Also perform multiplication or division if it is the last operator.
    stack.append(number)
    if operators and operators[-1] in mulOrDiv:
        snd = stack.pop()
        fst = stack.pop()
        operator = operators.pop()

        stack.append(mulOrDiv[operator](fst, snd))

    # The remaining computations are addition or subtraction. Perform these
    # in order from left to right.
    result = stack[0]
    for snd, operator in zip(stack[1:], operators):
        result = plusOrMinus[operator](result, snd)
        
    return result
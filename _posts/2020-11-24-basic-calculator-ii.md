---
title: Basic calculator ii
date: 2020-11-24
shortname: basic_calculator_ii
leetcode: https://leetcode.com/problems/basic-calculator-ii
tags: [stack]
---

## Problem

> Implement a basic calculator to evaluate a simple expression string.
> 
> The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces ` `.
> The integer division should truncate toward zero.

## Some questions to ask

* Is the expression guaranteed to be well-formed?

## Approach

Scan the expression from left to right. Use a stack to keep track of each parsed number and operator.

Whenever you encounter a new operator, check to see if the previous one was a high-precedence operator
(i.e. `*` or `/`) -- if so, pop the operator and the previous 2 numbers and push the computation
onto the respective stack. This guarantees that we prioritise the evaluation of subexpressions involving `*` or `/`.

At the end, the `operators` stack will be left with addition and subtraction, which we can use to process
the remaining numbers in the stack. 

```python
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
```

### Complexity
Let n be the length of the expression.

* O(n) time complexity, from traversing the string
* O(n) space complexity, from the stacks used for numbers and operators
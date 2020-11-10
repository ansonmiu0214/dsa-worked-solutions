---
title: Maximum frequency stack
date: 2020-11-10
shortname: max_freq_stack
leetcode: https://leetcode.com/problems/maximum-frequency-stack
tags: [stack, data structure]
---

## Problem

> Implement `FreqStack`, a class which simulates the operation of a stack-like data structure.
> 
> `FreqStack` has two functions:
> 
> * `push(int x)`, which pushes an integer `x` onto the stack.
> * `pop()`, which removes and returns the most frequent element in the stack.
>   * If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

## Some questions to ask

* What to return when popping an empty stack?

## Approach

Need a way to keep track of each item's frequency, as well as
the time at which each item is pushed onto the stack along with
its frequency at the time.

Stack operations should also have constant time complexity.

* We can keep track of each item's frequency using a dictionary,
  where getting and setting values run in constant time.
* Because the `pop()` operation pops the most frequent item,
  we can store the elements in a stack based on frequency.
  * As it is possible to have more than one most-frequent element,
  we can represent this as a __stack of (frequency) stacks__,
  and pushing an element onto the stack means pushing it onto
  the stack of its new frequency.

```python
class FreqStack:

    def __init__(self):
        self._itemToFreq = Counter()
        self._freqStack = [[]]

    def push(self, x: int) -> None:
        """Push integer 'x' onto the stack."""

        # Update item frequency.
        newFreq = self._itemToFreq[x] + 1
        self._itemToFreq[x] = newFreq

        # Push item into frequency stack corresponding
        # to new frequency, create if necessary.
        if newFreq == len(self._freqStack):
            self._freqStack.append([x])
        else:
            self._freqStack[newFreq].append(x)

    def pop(self) -> int:
        """Removes and returns the most frequent element. If
        there is a tie, the most recent element is returned."""

        # Remove item from stack with highest frequency.
        item = self._freqStack[-1].pop()
        self._itemToFreq[item] -= 1

        # Remove frequency stack if empty.
        if len(self._freqStack[-1]) == 0:
            self._freqStack.pop()

        return item
```

### Complexity

Let n be the number of elements in `FreqStack`. Note that after
`freqStack.push(3); freqStack.push(3);`, there are __2__ elements in
the stack.

* O(1) time complexity, from stack push/pop and dictionary get/set operations
* O(n) space complexity, as we keep track of history

### Other approaches

I first tried a stack of doubly-linked lists (DLL), where each
frequency has its own DLL. The solution would not store duplicate
elements, but rather, when `push`ing a new element into the stack,
it will remove the element's node from the currency frequency DLL
and append it to the successor frequency DLL.

The problem is that, for `pop` operations, we need to 'demote'
the element-to-be-popped into its predecessor frequency DLL,
but we lose information regarding its previous position.
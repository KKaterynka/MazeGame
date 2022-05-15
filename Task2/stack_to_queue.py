"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Transforms stack
    to queue
    """
    queue = ArrayQueue()
    lst = [item for item in stack][::-1]
    for item in lst:
        queue.add(item)
    return queue

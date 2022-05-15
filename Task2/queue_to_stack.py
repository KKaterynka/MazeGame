"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    Transforms queue
    to stack
    """
    stack = ArrayStack()
    lst = [item for item in queue][::-1]
    for item in lst:
        stack.push(item)
    return stack

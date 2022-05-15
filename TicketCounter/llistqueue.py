class Queue:
    """
    Implementation of the Queue ADT
    using a linked list
    """
    def __init__(self):
        """
        Creates an empty queue
        """
        self._qhead = None
        self._qtail = None
        self._count = 0

    def is_empty(self):
        """
        Returns True
        if the queue is empty
        """
        return self._qhead is None

    def __len__(self):
        """
        Returns the number
        of items in the queue
        """
        return self._count

    def enqueue(self, item):
        """
        Adds the given item to the queue
        """
        node = _QueueNode(item)
        if self.is_empty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    def dequeue(self):
        """
        Removes and returns
        the first item in the queue
        """
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
            self._qhead = self._qhead.next
            self._count -= 1
            return node.item


class _QueueNode:
    """
    Private storage class for
    creating the linked list nodes
    """
    def __init__(self, item):
        self.item = item
        self.next = None
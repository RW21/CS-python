from data_structures.linked_list import Node


class Stack:
    def __init__(self):
        self.last: Node
        self.number_of_nodes = 0

    def __len__(self):
        return self.number_of_nodes

    def __str__(self):
        return str(self.last)

    def pop(self):
        if self.number_of_nodes == 0:
            raise StackEmptyException
        val = self.last.val
        self.last = self.last.next
        self.number_of_nodes -= 1

        return val

    def push(self, item):
        if self.number_of_nodes == 0:
            self.last = Node(item)
        else:
            n = Node(item)
            n.next = self.last
            self.last = n

        self.number_of_nodes += 1

    def peek(self):
        return self.last.val


class StackEmptyException(Exception):
    """
    Stack is empty. Cannot pop anymore.
    """

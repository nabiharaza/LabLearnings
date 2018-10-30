from node import Node


class Stack:
    def __slots__ =

    ("head")

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self):
        newNode = Node
        if self.head is None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head = newNode

    def delete(self):
        assert not self.is_empty(), "Stack is Empty"

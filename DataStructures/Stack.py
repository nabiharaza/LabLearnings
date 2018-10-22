"""
stack.py
description: A linked stack (LIFO) implementation
"""

from node import LinkedNode


class Stack:
    __slots__ = "top"

    def __init__(self):
        """ Create a new empty stack.
        """
        self.top = None

    def __str__(self):
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        result = "Stack["
        n = self.top
        while n != None:
            result += " " + str(n.value)
            n = n.link
        result += " ]"
        return result

    def is_empty(self):
        return self.top == None

    def push(self, newValue):
        self.top = LinkedNode(newValue, self.top)

    def pop(self):
        assert not self.is_empty(), "Pop from empty stack"
        self.top = self.top.link

    def peek(self):
        assert not self.is_empty(), "peek on empty stack"
        return self.top.value

    insert = push
    remove = pop


def test():
    s = Stack()
    print(s)
    for value in 1, 2, 3:
        s.push(value)
        print(s)
    print("Popping:", s.peek())
    s.pop()
    print(s)
    for value in 15, 16:
        s.insert(value)
        print(s)
    print("Removing:", s.peek())
    s.remove()
    print(s)
    while not s.is_empty():
        print("Popping:", s.peek())
        s.pop()
        print(s)
    print("Trying one too many pops... ")
    try:
        s.pop()
        print("Problem: it succeeded!")
    except Exception as e:
        print("Exception was '" + str(e) + "'")


if __name__ == "__main__":
    test()

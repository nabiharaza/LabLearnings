from node import Node


class Queue:
    __slots__ = ("head", "tail")

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.link = newNode
            self.tail = newNode

    def dequeue(self):
        assert not self.is_empty(), "Queue is Empty!"
        self.head = self.head.link
        if self.head == None:
            self.tail = None

    def display(self):
        n = self.head
        while (n != None):
            print n.data
            n = n.link


def test():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    print "----------"
    q.dequeue()
    q.display()


if __name__ == "__main__":
    test()

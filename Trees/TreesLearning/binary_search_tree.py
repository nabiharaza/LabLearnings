from btnode import BTNode


class BST:
    __slots__ = "root", "size"

    def __init__(self):
        self.root = None
        self.size = 0

    def __insert(self, value, root):
        if value < self.root.value:
            if root.left is None:
                root.left = BTNode(value)
                print ("inserted at left: " + str(root.left.value))
            else:
                self.__insert(value, root.left)
        else:
            if root.right is None:
                root.right = BTNode(value)
                print ("inserted at right: " + str(root.right.value))
            else:
                self.__insert(value, root.right)

    def insert(self, value):
        if self.root is None:
            self.root = BTNode(value)
        else:
            self.__insert(value, self.root)


def test_BST():
    a = BST()
    a.insert(10)
    a.insert(9)
    a.insert(30)


if __name__ == '__main__':
    test_BST()

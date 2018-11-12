from btnode import BTNode


class BST:
    __slots__ = "root", "size"

    def __init__(self):
        self.root = None
        self.size = 0

    def __insert(self, value, root):
        if value < root.value:
            if root.left is None:
                root.left = BTNode(value)
                print ("Parent: " + str(root.value) + " --- Child Inserted at left: " + str(root.left.value))
            else:
                self.__insert(value, root.left)
        else:
            if root.right is None:
                root.right = BTNode(value)
                print ("Parent: " + str(root.value) + " --- Child at right: " + str(root.right.value))
            else:
                self.__insert(value, root.right)

    def insert(self, value):
        if self.root is None:
            self.root = BTNode(value)
        else:
            self.__insert(value, self.root)
        self.size = self.size + 1



def test_BST():
    a = BST()
    for values in (12, 90, 2, 5, 100, 4, 6):
        a.insert(values)
    print ("Size of the tree: " + str(a.size))


if __name__ == '__main__':
    test_BST()

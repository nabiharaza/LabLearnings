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

    def __contains(self, value, root):
        print "\n"
        parent = ""
        if root == None:
            print ("Sorry couldn't find")
        elif root.value == value:
            print ("Aha! Found you!")
        elif root.value > value:
            print ("Finding in left: Current Node:  -->" + str(root.value))
            parent = root
            print "---PARENT --- " + str(parent.value)
            self.__contains(value, root.left)
        elif root.value < value:
            print ("Finding in right : Current Node:  -->" + str(root.value))
            parent = root
            print "---PARENT --- " + str(parent.value)
            self.__contains(value, root.right)
        else:
            pass
        return

    def contains(self, value):
        if self.root == None:
            print "My tree is empty"
        else:
            self.__contains(value, self.root)

    def __height(self, root):
        if root == None:
            return -1
        else:
            return 1 + max(self.__height(root.left), self.__height(root.right))

    def height(self):
        return self.__height(self.root)


def test_BST():
    a = BST()
    for values in (12, 90, 2, 5, 100, 4, 6):
        a.insert(values)
    # print ("Size of the tree: " + str(a.size))
    a.contains(5)
    h = a.height()
    print ("Height of the tree is: "(str(h)))


if __name__ == '__main__':
    test_BST()

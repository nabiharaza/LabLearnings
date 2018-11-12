class BTNode:
    __slots__ = "value", "left", "right"

    def init(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def test_BTNode():
    parent = BTNode(10)
    left = BTNode(20)
    right = BTNode(30)
    parent.left = left
    parent.right = right
    print (parent.value)
    print (parent.left.value)
    print (parent.right.value)


if __name__ == '__main__':
    test_BTNode()

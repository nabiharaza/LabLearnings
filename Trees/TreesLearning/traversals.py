from btnode import BTNode


def inorder(root):  # LCR
    if root != None:
        inorder(root.left)
        print (root.value),
        inorder(root.right)


def preorder(root):  # CLR
    if root != None:
        print (root.value),
        preorder(root.left)
        preorder(root.right)


def postorder(root):  # LRC
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print (root.value),


def traverse(root):
    print("\n postorder")
    postorder(root)
    print ("\n preorder")
    preorder(root)
    print ("\n inorder ")
    inorder(root)


def test_traversal():
    traverse(BTNode('A',
                    BTNode('B',
                           BTNode('D'),
                           BTNode('E',
                                  BTNode('I'),
                                  BTNode('J'))),
                    BTNode('C',
                           BTNode('G',
                                  BTNode('K')),
                           BTNode('H'))))





if __name__ == "__main__":
    test_traversal()

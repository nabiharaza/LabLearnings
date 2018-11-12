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
    # b = BTNode(10)
    # BTNode(10, BTNode(20,BTNode,50,30)),BTNode
    # inorder(BTNode('A', BTNode('B'), BTNode('C')))
    traverse(BTNode(2,
                    BTNode(7,
                           BTNode(2),
                           BTNode(6,
                                  BTNode(5),
                                  BTNode(11))),
                    BTNode(5,
                           None,
                           BTNode(9,
                                  BTNode(4),
                                  None))))

    # traverse(BTNode('A',
    #                 BTNode('B',
    #                        None,
    #                        BTNode('D')),
    #                 BTNode('C',
    #                        BTNode('E',
    #                               BTNode('G'),
    #                               None),
    #                        BTNode('F',
    #                               BTNode('H'),
    #                               BTNode('I')))))


if __name__ == "__main__":
    test_traversal()

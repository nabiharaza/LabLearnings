from btnode import BTNode

level = 0


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


def display_leaves(root):
    if root != None:
        if root.left == None and root.right == None:
            print(root.value),
        else:
            display_leaves(root.left)
            display_leaves(root.right)


def display_parents(root):
    if root != None:
        if root.left == None and root.right == None:
            pass
        else:
            print (root.value),
            display_parents(root.left)
            display_parents(root.right)


def display_same_height_nodes(root, k):
    if root is None:
        return
    if k == 0:
        print root.value,
    else:
        display_same_height_nodes(root.left, k - 1)
        display_same_height_nodes(root.right, k - 1)


def traverse(root):
    print("\n postorder")
    postorder(root)
    print ("\n preorder")
    preorder(root)
    print ("\n inorder ")
    inorder(root)
    print ("\n\n Display Leaves")
    display_leaves(root)
    print ("\n\n Display only parents")
    display_parents(root)
    print ("\n\n Display nodes at the same height")
    display_same_height_nodes(root, 2)


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

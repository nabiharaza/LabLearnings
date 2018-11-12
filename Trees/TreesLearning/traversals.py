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
    elif k > 0:
        display_same_height_nodes(root.left, k - 1)
        display_same_height_nodes(root.right, k - 1)


def print_reverse_tree(root):
    h = height(root)
    for i in reversed(range(1, h + 1)):
        display_same_height_nodes(root, i)


def __height(root):
    if root == None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


def height(root):
    return __height(root)


def __contains(root, value, level):
    if root is None:
        return level
    elif root.value == value:
        return level
    elif root.value > value:
        return __contains(root.left, value, level + 1)
    elif root.value < value:
        return __contains(root.right, value, level + 1)


def find_deepest_node(root, level, max_level, current_deep_root):
    if root != None:
        find_deepest_node(root.left, level + 1, max_level, current_deep_root)
        if level > max_level:
            current_deep_root = root.value
            max_level = level
        find_deepest_node(root.right, level, max_level, current_deep_root)


def print_deepest_node(root):
    res = -1
    maxLevel = -1
    find_deepest_node(root, 0, maxLevel, res)
    return res


def contains(root, value):
    return __contains(root, value, 0)


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
    print ("\n\nheight of the tree")
    print (height(root))

    print ("\n\n Print Reversel")
    print_reverse_tree(root)

    print ("\n\n contains at level")
    Level = contains(root, 'E')
    print Level

    print ("\n\n Deepest node")
    print (print_deepest_node(root))


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

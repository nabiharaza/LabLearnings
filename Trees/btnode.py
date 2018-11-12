"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""


class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'val', 'left', 'right'

    def __init__(self, val, left=None, right=None):
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right


def testBTNode():
    """
    A test function for BTNode.
    :return: None
    """
    parent = BTNode(10)
    left = BTNode(20)
    right = BTNode(30)
    parent.left = left
    parent.right = right
    print('parent (30):', parent.val)
    print('left (10):', parent.left.val)
    print('right (20):', parent.right.val)


if __name__ == '__main__':
    testBTNode()

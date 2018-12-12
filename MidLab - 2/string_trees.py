class TNode:
    __slots__ = "root", "list_of_tree_nodes", "list_of_matching_nodes"

    def __init__(self, root, tree_nodes=None):
        self.root = root
        self.list_of_tree_nodes = tree_nodes

    def __str__(self):
        # traversing back to the list
        if self.root != None:
            self.list_of_tree_nodes.append(self.root)

    def parse_tree(self):
        list_tree = raw_input("Enter tree list: ")
        for i in list_tree:
            if type(i) is not list_tree:
                if self.root == None:
                    tNode = TNode(self.list_of_tree_nodes)
            else:
                self.__parse_tree(self.root, i + 1)

    def __parse_tree(self, root, child):
        tNode = TNode()
        tNode.list_of_tree_nodes = tNode.list_of_tree_nodes.append(child)  # adding the children list to the root object

    def match(self, root):

        match_list = raw_input("Enter tree list to match: ").split()
        for i in match_list:
            if match_list[i] != self.root:
                print ("The root is not matching")
                return False
                break

            elif match_list[i] == self.root:
                return True
            else:
                self.match(self, self.root)

    def get_matches(self, seq):
        seq = seq.split()
        for i in seq:
            line = seq[i]
            if self.root == seq[i]:
                continue
            else:
                break
        return


def main():
    a = TNode('a')
    a.parse_tree()
    tree = a.parse(eval(input("Enter a tree")))
    w = input('Enter a sequence:').split()
    m = tree.get.mactches(w)

    print ('Tree', tree, 'has', len(m), 'matches')
    for t in m:
        print (t)


if __name__ == "__main__":
    main()

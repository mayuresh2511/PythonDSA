
class Node:

    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


class BinaryTreeImpl:

    def __init__(self, root):
        self.root = Node(root)



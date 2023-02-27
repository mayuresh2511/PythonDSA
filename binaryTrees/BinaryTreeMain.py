from binaryTrees.BinaryTree import BinaryTreeImpl
from binaryTrees.BinaryTree import Node
from queue.QueueImpl import Queue
from Stack.Stack import Stack


bt = BinaryTreeImpl(1);
bt.root.left_node = Node(2)
bt.root.right_node = Node(3)
bt.root.left_node.left_node = Node(4)
bt.root.left_node.right_node = Node(5)
bt.root.right_node.left_node = Node(6)
bt.root.right_node.right_node = Node(7)


def binary_tree_pre_order_traversal(root: Node):

    if root is None:
        return

    print(root.data)
    binary_tree_pre_order_traversal(root.left_node)
    binary_tree_pre_order_traversal(root.right_node)


# binary_tree_pre_order_traversal(bt.root)

def binary_tree_in_order_traversal(root: Node):

    if root is None:
        return

    binary_tree_in_order_traversal(root.left_node)
    print(root.data)
    binary_tree_in_order_traversal(root.right_node)

# binary_tree_in_order_traversal(bt.root)


def binary_tree_post_order_traversal(root: Node):

    if root is None:
        return

    binary_tree_post_order_traversal(root.left_node)
    binary_tree_post_order_traversal(root.right_node)
    print(root.data)


# binary_tree_post_order_traversal(bt.root)

def binary_tree_level_order_traversal(root: Node):

    level_queue = Queue()

    level_queue.enqueue(root)

    while not level_queue.is_empty() and level_queue.peek() is not None:

        node = level_queue.dequeue()
        level_queue.enqueue(node.left_node)
        level_queue.enqueue(node.right_node)
        print(node.data)


# binary_tree_level_order_traversal(bt.root)

def binary_tree_reverse_level_traversal(root: Node):

    level_stack = Stack()
    level_queue = Queue()

    level_queue.enqueue(root)

    while not level_queue.is_empty() and level_queue.peek() is not None:

        node = level_queue.dequeue()
        level_queue.enqueue(node.right_node)
        level_queue.enqueue(node.left_node)
        level_stack.push(node.data)

    while not level_stack.is_empty():

        print(level_stack.pop())


# binary_tree_reverse_level_traversal(bt.root)

def binary_tree_height(root: Node):

    if root is None:
        return 0

    left_height = binary_tree_height(root.left_node)
    right_height = binary_tree_height(root.right_node)

    return 1 + max(left_height, right_height)

def binary_Tree_Size(root: Node):

    if root is None:
        return 0

    left_size = binary_Tree_Size(root.left_node)
    right_size = binary_Tree_Size(root.right_node)

    return 1 + left_size + right_size

def bianry_Tree_Size_Iterative(root: Node):

    queue = Queue()
    binary_tree_size = 0

    queue.enqueue(root)

    while queue.is_empty() is not True:

        curr_node = queue.dequeue()
        binary_tree_size = binary_tree_size + 1

        if curr_node.left_node is not None:
            queue.enqueue(curr_node.left_node)

        if curr_node.right_node is not None:
            queue.enqueue(curr_node.right_node)

    return binary_tree_size


print(bianry_Tree_Size_Iterative(bt.root))







class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        if self.head is None:
            self.head = Node(data)
            return
        elif self.head.get_next_node() is None:
            self.head.next_node = Node(data)
            return

        curr_node = self.head
        while curr_node.get_next_node() is not None:

            curr_node = curr_node.get_next_node()

        curr_node.set_next_node(Node(data))

        return

    def prepend(self, data):

        if self.head is None:
            self.head = Node(data)
            return

        new_head = Node(data)
        new_head.next_node = self.head
        self.head = new_head

    #  traverse linked list function   ####
    def traverse_list(self):

        if self.head is None:
            return None

        curr_node = self.head

        while curr_node is not None:

            print(curr_node.get_data())
            curr_node = curr_node.get_next_node()

        return

    #  insert node in linked list function   ####
    def insert_after_node(self, prev_node, data):

        curr_node = self.head
        new_node = Node(data)

        while (curr_node is not None) and (curr_node.data != prev_node):
            curr_node = curr_node.next_node

        curr_node_next_node = curr_node.next_node
        new_node.next_node = curr_node_next_node
        curr_node.next_node = new_node

    #  delete node of linked list function   ####
    def delete_node(self, data):

        if self.head.data == data:
            self.head = self.head.next_node
            return

        curr_node = self.head

        while (curr_node is not None) and (curr_node.data != data):

            prev_node = curr_node
            curr_node = curr_node.next_node

        prev_node.next_node = curr_node.next_node
        curr_node = None

    #  find length of linked list function   ####
    def find_length(self):

        linked_list_lrngth = 0

        curr_node = self.head

        while curr_node is not None:

            linked_list_lrngth += 1
            curr_node = curr_node.next_node

        return linked_list_lrngth

    #  find length recursive way of linked list function   ####
    def find_length_recursive(self, head_node):

        if head_node is None:
            return 0

        return self.find_length_recursive(head_node.next_node) + 1

    #  Swap linked list nodes function   ####

    def swap_nodes(self, nodeA_data, nodeB_data):

        list_of_nodes = []

        curr_node = self.head
        prev_node = None

        while curr_node is not None:

            if curr_node.data == nodeA_data:
                list_of_nodes.append(prev_node)
                list_of_nodes.append(curr_node)

            if curr_node.data == nodeB_data:
                list_of_nodes.append(prev_node)
                list_of_nodes.append(curr_node)

            prev_node = curr_node
            curr_node = curr_node.next_node

        list_of_nodes[0].next_node = list_of_nodes[3]
        print(str(list_of_nodes[0].data) + " -> " + str(list_of_nodes[3].data) + " ->" + str(list_of_nodes[3].next_node.data))
        list_of_nodes[2].next_node = list_of_nodes[1]
        print(str(list_of_nodes[2].data) + " -> " + str(list_of_nodes[1].data) + " ->" + str(list_of_nodes[1].next_node.data))
        list_of_nodes[1].next_node, list_of_nodes[3].next_node = list_of_nodes[3].next_node, list_of_nodes[1].next_node

        list_of_nodes = None

#  Reverse linked list function   ####

    def reverse_linked_list(self):

        curr_node = self.head
        prev_node = None
        next_node = None

        while curr_node is not None:

            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def reverse_linked_list_recursive(self, head_node):

        if head_node is None:
            return None

        curr_node = self.reverse_linked_list_recursive(head_node.next_node)

        if curr_node is not None:
            curr_node.next_node = head_node
            head_node.next_node = None
            return head_node
        else:
            self.head = head_node
            return head_node


if __name__ == "main":
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)

    linked_list.prepend(0)

    linked_list.insert_after_node(3, 4)

    # linked_list.delete_node(0)
    #
    # print("Linked list length : " + str(linked_list.find_length()))
    # print("Linked list length : " + str(linked_list.find_length_recursive(linked_list.head)))

    # linked_list.swap_nodes(3, 4)

    # linked_list.reverse_linked_list()

    linked_list.reverse_linked_list_recursive(linked_list.head)

    linked_list.traverse_list()

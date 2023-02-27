
def remove_duplicate(linked_list):

    curr_node = linked_list.head

    while curr_node is not None:

        new_curr_node = curr_node.next_node
        prev_node = curr_node

        while new_curr_node is not None:

            if curr_node.data == new_curr_node.data:
                prev_node.next_node = new_curr_node.next_node

            prev_node = new_curr_node
            new_curr_node = new_curr_node.next_node

        curr_node = curr_node.next_node

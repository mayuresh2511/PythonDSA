from LinkedList.LinkedListImpl import LinkedList


def merge_sorted_linked_lists(linked_list_a, linked_list_b):

    merged_linked_list = LinkedList()
    curr_node_a = linked_list_a.head
    curr_node_b = linked_list_b.head

    while curr_node_a is not None and curr_node_b is not None:

        if curr_node_a.data < curr_node_b.data:
            merged_linked_list.append(curr_node_a.data)
            curr_node_a = curr_node_a.next_node

        if curr_node_b.data < curr_node_a.data:
            merged_linked_list.append(curr_node_b.data)
            curr_node_b = curr_node_b.next_node

    if curr_node_a is not None:

        while curr_node_a is not None:
            merged_linked_list.append(curr_node_a.data)
            curr_node_a = curr_node_a.next_node

    if curr_node_b is not None:

        while curr_node_b is not None:
            merged_linked_list.append(curr_node_b.data)
            curr_node_b = curr_node_b.next_node

    return merged_linked_list

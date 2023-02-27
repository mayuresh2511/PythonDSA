from LinkedList.LinkedListImpl import LinkedList
from LinkedList.mergeSortedLinkedLists import merge_sorted_linked_lists
from LinkedList.RemoveDuplicate import remove_duplicate

''' Calling merge_sorted_linked_lists function '''

linked_list_A = LinkedList()

linked_list_A.append(1)
linked_list_A.append(5)
linked_list_A.append(6)
linked_list_A.append(8)

linked_list_B = LinkedList()

linked_list_B.append(2)
linked_list_B.append(3)
linked_list_B.append(4)
linked_list_B.append(7)

# merged_linked_list = merge_sorted_linked_lists(linked_list_A, linked_list_B)
# merged_linked_list.traverse_list()

''' Calling remove_duplicate function from RemoveDuplicate '''

linked_list_with_duplicates = LinkedList()

linked_list_with_duplicates.append(1)
linked_list_with_duplicates.append(6)
linked_list_with_duplicates.append(1)
linked_list_with_duplicates.append(4)
linked_list_with_duplicates.append(2)
linked_list_with_duplicates.append(2)
linked_list_with_duplicates.append(4)

remove_duplicate(linked_list_with_duplicates)

linked_list_with_duplicates.traverse_list()
from Linked_list import LinkedList


def remove_duplicate(head):
    current_node = head.next
    prev_node = head

    while current_node:
        if current_node.data != prev_node.data:
            prev_node.next = current_node
            prev_node = current_node
        current_node = current_node.next
    prev_node.next = current_node
    return head


def remove_duplicate_recursive(head):
    if not head or not head.next:
        return head
    head.next = remove_duplicate_recursive(head.next)
    return head.next if head.data == head.next.data else head


link_list = LinkedList()
link_list.makeLinkedList([1, 1, 1, 2, 2, 3, 3])
link_list.print_format()
link_list.head = remove_duplicate_recursive(link_list.head)
# print(link_list.head.data, link_list.head.next.data)
link_list.print_format()

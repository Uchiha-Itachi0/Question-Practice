from Linked_list import LinkedList


# Solved by creating new linked list
def merge_two_sorted_linked_list(head1, head2) -> LinkedList:
    new_linked_list = LinkedList()
    while head1 and head2:
        if head1.data <= head2.data:
            new_linked_list.append(head1.data)
            head1 = head1.next
        else:
            new_linked_list.append(head2.data)
            head2 = head2.next

    if head1:
        new_linked_list.append(head1.data)
    elif head2:
        new_linked_list.append(head2.data)

    return new_linked_list


head1 = LinkedList()
head2 = LinkedList()
head1.makeLinkedList([1, 2, 3])
head2.makeLinkedList([0, 1, 3, 4])
new_head = merge_two_sorted_linked_list(head1.head, head2.head)
new_head.print_format()
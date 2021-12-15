# Using merge sort is provide in the linked list file itself
from Linked_list import LinkedList


def calculate_the_length(head: LinkedList) -> int:
    current_node = head
    count = 0
    while current_node:
        count += 1
        current_node += 1
    return count


def sorting(head: LinkedList):
    """
    Sorting using bubble sort
    Time Complexity : O(n^2)
    Auxiliary space Complexity : O(1)
    """
    if not head:
        return

    length = calculate_the_length(head)
    if head and head.next.next:
        if head.next.next.data <= head.next.data:
            head.next, head.next.next = head.next.next, head.next
        sorting(head.next)


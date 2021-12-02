from Linked_list import LinkedList


# A simple program using set to keep track of the visited nodes
def find_circle_in_linked_list(head: LinkedList) -> bool:
    storage = set()
    count = 0
    while head:
        if count != len(storage):
            return True
        count += 1
        storage.add(head)
        head = head.next
    return False


# Using fast and slow pointer approach
def find_circle_in_linked_list_2(head: LinkedList) -> bool:
    pointer_1 = head
    pointer_2 = head
    # If list is empty then this will take care of it
    while pointer_2 and pointer_2.next:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next.next
        if pointer_1 == pointer_2:
            return True
    return False


linkedList = LinkedList()
linkedList.makeLinkedList([0])
linkedList.makeCircle(-1)
# print(find_circle_in_linked_list(linkedList.head))
print(find_circle_in_linked_list_2(linkedList.head))

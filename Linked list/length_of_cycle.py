from Linked_list import LinkedList


def calculate_length(fast, slow):
    count = 1
    while fast != slow:
        count += 1
        slow = slow.next
    return count


def length_of_cycle(head: LinkedList) -> int:
    fast = head
    slow = head
    while True:
        fast = fast.next.next
        slow = slow.next.next
        if fast == slow:
            return calculate_length(fast, slow.next)


linkedList = LinkedList()
linkedList.makeLinkedList([1])
linkedList.makeCircle(0)
print(length_of_cycle(linkedList.head))

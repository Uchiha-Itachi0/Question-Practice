from Linked_list import LinkedList


# Let say cycle start from 4
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 4 -> ...
# Move forward by length of cycle
# f = 1, s = 5
# Now keep moving f and s till both are equal
# They will meet at the start of cycle

# Calculating the length of the list
def __calculate_length(fast, slow):
    length = 1
    while slow != fast:
        length += 1
        slow = slow.next
    return length


# Calculating the length of the list
def __cycle_length(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return __calculate_length(fast, slow.next)
    return


def start_of_cycle(head: LinkedList) -> int:
    # First we need to calculate the length of the cycle
    length = __cycle_length(head)
    if not length:
        return -1
    f = head
    s = head

    # Moving s to the length of the list
    while length > 0:
        s = s.next
        length -= 1
    # Moving both till they are equal
    while f != s:
        f_data = f.data
        s_data = s.data
        f = f.next
        s = s.next
    return f.data


linkedList = LinkedList()
linkedList.makeLinkedList([1, 2, 3, 4, 5, 6, 7])
linkedList.makeCircle(5)
print(start_of_cycle(linkedList.head))

from Linked_list import LinkedList


# By calculating the length of the linked list
def calculate_the_mid(head: LinkedList) -> int:
    mid = linkedList.length() // 2
    count = 0
    while head:
        if count == mid:
            return head.data
        head = head.next
        count += 1


# By using fast and slow pointer approach
# If someone is moving twice as fast as you then when they cover full distance
# Then you definitely would have covered half the distance
def calculate_the_mid_2(head: LinkedList) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data


linkedList = LinkedList()
linkedList.makeLinkedList([1, 2, 3, 4, 5])
print(calculate_the_mid_2(linkedList.head))

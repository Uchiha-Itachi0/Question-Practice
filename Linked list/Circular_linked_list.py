class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        # If list already contains some element
        if self.head:
            self.tail.next, new_node.next, self.tail = new_node, self.head, new_node
        else:
            self.head = self.tail = new_node
            self.head.next, self.tail.next = self.tail, self.head

    def length(self):
        current_node = self.head
        count = 0
        if not current_node:
            return count
        else:
            while current_node.next != self.head:
                count += 1
                current_node = current_node.next
            return count + 1

    def insert(self, data, index):
        current_node = self.head
        previous_node = None
        new_node = Node(data)
        count = 0
        # if we are inserting at index 0 then we can simply point head to the new node
        if index == 0:
            self.head, new_node.next = new_node, self.head

            # Updating the tail to point to the new head
            self.tail.next = self.head
        elif index >= self.length():
            self.tail.next, new_node.next = new_node, self.head

        else:
            # Since we are taking care of all number >= length so this loop will not run infinite.
            while current_node:
                if count == index:
                    previous_node.next, new_node.next = new_node, current_node
                    # As soon as we insert the element we have to exit the loop because this is
                    # a circular linked list and no node points to none so this loop will never end
                    return
                count += 1
                previous_node = current_node
                current_node = current_node.next

    def delete(self, index):
        # Since we are taking care of index 0 separately therefore we set the count value to 1 because
        # we care counting from index 1
        current_node, previous_node, count = self.head.next, None, 1

        # if we have to delete the first element then we can simply shifts the head to point to next node
        if index == 0:
            self.head = self.head.next

            # Updating tail to point to new head
            self.tail.next = self.head
        else:
            while current_node != self.head:
                if count == index:
                    previous_node.next = current_node.next
                    return
                count += 1
                previous_node = current_node
                current_node = current_node.next

    def print_in_format(self):
        current_node = self.head
        if not current_node:
            print('Circular linked list is empty')
        else:
            # If the next node is head that means we have reached the head again.
            while current_node.next != self.head:
                print(f'{current_node.data} ->', end=' ')
                current_node = current_node.next
            # If the next val is head than the loop breaks and the current node whose next is head
            # does not print Therefore we print it outside the loop.
            print(f'{current_node.data} -> CONTINUE')


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
# print(cll.length())
# cll.insert(0, 0)
cll.delete(2)
# print(cll.tail.next.data)
cll.print_in_format()

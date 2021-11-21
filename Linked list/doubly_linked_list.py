class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        # If head is already defined means if linked list is not empty
        if self.head:
            new_node = Node(data)

            # setting the pointer of tail to new created node
            # and setting the prev pointer of new created node to tail as
            # doubly linked list knows about it previous data
            self.tail.next, new_node.prev = new_node, self.tail

            # moving tail forward, tail always contain object of last node
            self.tail = new_node

        # if head is not defined that means linked list is empty
        # Therefore we have to set head and tail to newly created node
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def insert(self, data, index):

        new_node = Node(data)
        # if the index is 0 then we can simply change the value of the head pointer
        # to point to the new data
        if index == 0:
            """
            head.prev -> new_node
            new_node.next -> head
            head -> new_node
            """
            self.head, self.head.prev, new_node.next = new_node, new_node, self.head

        # if we have to insert at the last index than we can take the help of
        # tail which is always points to the last node in our linked list
        elif index >= self.length():
            self.tail.next, new_node.prev = new_node, self.tail
            self.tail = new_node

        # Otherwise we have to traverse the list to insert at any particular idex
        # Here we don't need any variable to point to prev node because doubly linked
        # list have prebuilt var that store the location and data of previous node
        else:
            current_node = self.head
            count = 0
            while current_node:
                if count == index:
                    current_node.prev.next, new_node.prev, new_node.next, current_node.prev = new_node, current_node.prev, current_node, new_node
                count += 1
                current_node = current_node.next

    def delete(self, index):
        # If we are deleting at index 0 than we can simply move head to point
        # to the next node
        if index == 0:
            self.head, self.head.next.prev = self.head.next, None

        # If we are deleting from index >= length of linked list than we can take
        # the help from tail pointer
        elif index >= self.length() - 1:
            self.tail.prev.next, self.tail = None, self.tail.prev

        else:
            current_node = self.head
            count = 0
            while current_node:
                if count == index:
                    current_node.prev.next, current_node.next.prev = current_node.next, current_node.prev
                count += 1
                current_node = current_node.next

    def print_in_format(self):
        current_node = self.head
        while current_node:
            print(f'{current_node.data} ->', end=' ')
            current_node = current_node.next
        print('END')

    # For printing in reverse. To achieve this we can take help from tail
    def print_rev_in_format(self):
        current_node = self.tail
        while current_node:
            print(f'{current_node.data} ->', end=' ')
            current_node = current_node.prev
        print('END')


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.insert(2.5, 2)
# print(dll.length())
# dll.delete(78)
dll.print_rev_in_format()

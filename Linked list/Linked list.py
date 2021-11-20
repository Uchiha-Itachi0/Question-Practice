# It stores the data and the value to the next element
class Node:
    def __init__(self, data):
        self.data = data

        # when defined there is no data to point to
        self.next = None


# Main blue print for our linked list that contains all the method that will
# help us to make linked list
class LinkedList:
    def __init__(self):

        # Help us to append to the linked list
        self.tail = None

        # It points to the first element of the linked list
        self.head = None

    # This append method store the data in order that you entered
    def append(self, data):

        # If self head is not set to none means that the linked list is
        # not empty but it already points to some elements
        if self.head:

            # Creates a new node with data provided
            new_node = Node(data)

            # setting the previous node pointer to new node location
            self.tail.next = new_node

            # moving to location pointer to new node location so on next
            # append we can set this node pointer to new node object
            self.tail = new_node

        # if linked list is empty then we need to set the head to the appended
        # data
        else:
            node = Node(data)
            self.head = node
            self.tail = node

    # Append in front of the linked list
    def append_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Just travel through list
    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # inserting at particular index
    def insert(self, data, index):

        # if we have to insert at 0 index then we can take help from head pointer
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        # If we have to insert element in last index then we can take the help
        # from tail pointer
        elif index >= self.length():
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

        # Else we have to think otherwise
        else:
            current_node = self.head
            previous_node = None
            count = 0
            while current_node:
                if count == index:
                    new_node = Node(data)
                    previous_node.next, new_node.next = new_node, current_node
                    return
                count += 1
                previous_node = current_node
                current_node = current_node.next

    # deleting any particular index
    def delete(self, index):

        # if the index is 0 then we simply have to move the head to next element
        if index == 0:
            self.head = self.head.next

        # Otherwise we have to proceeds to our logic
        else:
            current_node = self.head
            previous_node = None
            count = 0
            while current_node:
                if count == index:
                    previous_node.next = current_node.next
                count += 1
                previous_node = current_node
                current_node = current_node.next

    # Getting all the value
    def getAll(self):
        current_node = self.head
        storage = []
        while current_node:
            storage.append(current_node.data)
            current_node = current_node.next
        return storage

    def print_format(self):
        current_node = self.head
        while current_node:
            print(f'{current_node.data} ->', end=' ')
            current_node = current_node.next
        print('END')


ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(5, 0)
ll.delete(10)
ll.print_format()

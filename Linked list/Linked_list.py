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

    # Forming linked list by passing values in list
    def makeLinkedList(self, data):
        for value in data:
            new_node = Node(value)
            if self.head:
                self.tail.next, new_node.next = new_node, None
                self.tail = new_node
            else:
                self.head, self.tail = new_node, new_node

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
        new_node = Node(data)

        # if we have to insert at 0 index then we can take help from head pointer
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        # If we have to insert element in last index then we can take the help
        # from tail pointer
        elif index >= self.length():
            self.tail.next = new_node
            self.tail = new_node

        # Else we have to think otherwise
        else:
            current_node = self.head
            previous_node = None
            count = 0
            while current_node:
                if count == index:
                    previous_node.next, new_node.next = new_node, current_node
                    return
                count += 1
                previous_node = current_node
                current_node = current_node.next

    # inserting at particular index using recursion
    def insert_with_recursion(self, data, index):
        new_node, current_node = Node(data), self.head

        # This helper function has None return type
        # self.__insert_helper(data, index, current_node, None, new_node, 0)

        # This helper function has Node(obj) return Type
        # Change the head to whatever is returned from the helper function
        self.head = self.__insert_helper_return(index, current_node, new_node)

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

    # Helper function for insert with recursion
    def __insert_helper(self, data, index, current_node, prev_node, new_node, count):

        # If index >= length then we can simply add element to the tail
        if index >= self.length():
            self.tail.next, new_node.next = new_node, None
            self.tail = new_node
            return

        # If index is 0 we can simply add element to the head
        elif index == 0:
            self.head, new_node.next = new_node, self.head
            return
        else:
            if index == count:
                prev_node.next, new_node.next = new_node, current_node
                return
            self.__insert_helper(data, index, current_node.next, current_node, new_node, count + 1)

    def __insert_helper_return(self, index, current_node, new_node):

        # If we want to insert at the end with index >= length then the logic will change
        if index >= 0 and current_node is None:
            new_node.next = None
            self.tail = new_node
            return new_node

        elif index == 0:
            new_node.next = current_node
            return new_node

        current_node.next = self.__insert_helper_return(index - 1, current_node.next, new_node)
        return current_node

    # This method just created to solve certain questions
    def makeCircle(self, index):
        current_node = self.head
        count = 0
        if index == -1:
            return
        elif index >= self.length():
            self.tail.next = self.tail
        while current_node:
            if index == count:
                self.tail.next = current_node
                return
            count += 1
            current_node = current_node.next



# ll = LinkedList()
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.insert_with_recursion(5, 0)
# # ll.delete(10)
# ll.print_format()

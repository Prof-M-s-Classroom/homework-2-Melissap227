from Spaceship import Spaceship


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #point the new node to the front of the list (the list's current head)
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
    def insert_at_index(self,value,index):
        if self.length < index or index < 1:
            return False

        elif self.length == 0 or index == 0:
            self.prepend(value)
            return True

        elif index == self.length - 1:
            self.append(value)
            return True

        else:
            newnode = Node(value)
            current = self.head
            for current in range(index - 1):
                current = current.next
            newnode.next = current.next
            current.next = newnode

            self.length += 1
            return True

# TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
    def del_at_index(self, index):

        if index < 1 or index > self.length:
            return None

        if index == 0:
            self.delfirst()

        if index == self.length - 1:
            self.dellast()

            current = self.head  # current node starts at the front

        for current in range(index - 1):
            current == current.next() #moves down the list

        current.next = current.next.next
        self.length -= 1



# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.


def testSpaceship():  # method to test Spaceship()
    s1 = Spaceship("Voyager", 300)
    s2 = Spaceship("Enterprise", 300)
    s3 = Spaceship("Atlantis", 300)
    s4 = Spaceship("Challenger", 300)
    s5 = Spaceship("Artemis", 300)

    mylinkedlist = LinkedList(s1)
    mylinkedlist.append(s2)
    mylinkedlist.append(s3)
    mylinkedlist.prepend(s4)
    mylinkedlist.prepend(s5)
    mylinkedlist.print_list()

testSpaceship()

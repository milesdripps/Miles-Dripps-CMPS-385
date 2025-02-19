# Miles Dripps
#
# University of La Verne
#
# CMPS 385: Singly Linked List Assignment

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #for testing purposesl
    def printlist(self):
        loop = self.head
        i = 0
        display_list = ""
        if loop is None:
            print("end of list / list empty")
            return 0
        while loop:
            display_list += (f" ({i})"+ str(loop.data))
            loop = loop.next
            i += 1
        print(display_list)

    #Creates a new node with the data, and places it into the index
    def insertnode(self, data, index):

        #initialize a new node object
        insert_node = Node(data)

        #for first index insertion
        if index == 0:
            #point inserted node to head node
            insert_node.next = self.head
            self.head = insert_node
            return 0

        if index > 0: #Iterate to index of node before insertioni point
            current_node = self.head
            for x in range(index-1):
                if current_node is None:
                    return 1
                current_node = current_node.next

            #point insert node to the node the current one points to
            insert_node.next = current_node.next
            #point the current node to the insert node
            current_node.next = insert_node
            return 0

    def deletenode(self, index):
        previous = self.head

        # To delet eth e first node in the list
        if index == 0:
            self.head = previous.next
            return 0

        # Same formula as inserting but with two new pointers
        for x in range(index-1):
            if previous is None:
                print("Index out of range")
                return 1
            previous = previous.next

        #check
        if previous is not None:
            current = previous.next
        else:
            return 1

            #Set the previous node to point to the node after the node it points to.
        previous.next = current.next

        #Clean up trash?
        current.data = 0
        current.next = None
        return 0

def main():
    #Test the lists

    list1 = LinkedList()
    print("**** Inserted into the front *****")
    list1.insertnode(10, 0)
    list1.printlist()
    list1.insertnode(27, 0)
    list1.printlist()
    list1.insertnode(1001, 0)
    list1.printlist()
    list1.insertnode(28, 0)
    list1.printlist()
    list1.insertnode(1, 0)
    list1.printlist()
    #The list should now be: 1,28,1001,27,10

    print("** Inserting 77 into index 3")
    list1.insertnode(77, 3)
    list1.printlist()
    #The list should now be: 1,28,1001,77,27,10

    print("*Deleting Node at index 0")
    list1.deletenode(0)
    list1.printlist()
    print("*Deleting Node at index 3")
    list1.deletenode(3)
    list1.printlist()


main()
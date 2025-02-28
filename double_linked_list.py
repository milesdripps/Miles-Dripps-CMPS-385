class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def DoubleLinkedListInsert(self, data, index):
        node = Node(data)

        # Insert at beginning
        if index == 0:
            node.next = self.head
            if self.head is not None:
                self.head.previous = node
            self.head = node
            return 0

        # Insert at a given index
        tmp = self.head
        for i in range(index - 1):
            if tmp is None:
                return -1
            tmp = tmp.next

        # insert at the index
        node.next = tmp.next
        if tmp.next is not None:
            tmp.next.previous = node
        tmp.next = node
        node.previous = tmp
        return 0

    def DoubleLinkedListDelete(self, index):
        if self.head is None:
            return -1  # Empty list

        tmp = self.head

        # Deleting the first node
        if index == 0:
            self.head = tmp.next
            if self.head is not None:
                self.head.previous = None
            return 0

        # search to the node to be deleted
        for i in range(index):
            tmp = tmp.next
            if tmp is None:
                return -1

        # Remove node from the list
        if tmp.next is not None:
            tmp.next.previous = tmp.previous
        if tmp.previous is not None:
            tmp.previous.next = tmp.next

        return 0

    def DoubleLinkedListDisplay(self):
        tmp = self.head
        display_list = []
        while tmp:
            display_list.append(str(tmp.data))
            tmp = tmp.next
        print(" <-> ".join(display_list))


def main():
    L1 = DoubleLinkedList()
    L1.DoubleLinkedListInsert(55, 0)
    L1.DoubleLinkedListInsert(77, 1)
    L1.DoubleLinkedListInsert(99, 1)
    L1.DoubleLinkedListInsert(33, 0)
    L1.DoubleLinkedListDisplay()

    L1.DoubleLinkedListDelete(2)
    L1.DoubleLinkedListDisplay()


if __name__ == "__main__":
    main()

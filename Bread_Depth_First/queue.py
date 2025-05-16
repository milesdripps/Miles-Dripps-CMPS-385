class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.previous = None

class Queue:
    def __init__(self):
        self.start = None
        self.last_node = None

    def empty(self):
        return self.start is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.empty():  # If the queue is initially empty
            self.start = new_node
            self.last_node = new_node
        else:
            # If the queue is not empty
            self.start.previous = new_node

            new_node.next = self.start
            self.start = new_node
        self.display()

    def dequeue(self):
        if self.empty():
            print("Queue is empty.")
            return None

        to_remove = self.last_node
        if to_remove.previous:
            self.last_node = to_remove.previous
            self.last_node.next = None
        else:
            # Only one node in the queue
            self.start = None
            self.last_node = None

        print(f"popped {to_remove.data}, new end node is {self.last_node.data if self.last_node else 'None'}")
        return to_remove.data

    def display(self):
        if self.start:
            top = self.start
            l = "EnQueue(start) ->"

            while top:
                l += f" [{top.data}] "
                top = top.next

            l += f" <- Dequeue/pop(end)"
            print(l)
        else:
            return

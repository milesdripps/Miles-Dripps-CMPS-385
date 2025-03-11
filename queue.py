class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.top = None  # front of queue

    def isEmpty(self):
        if self.top is None:
            print("Queue is empty")
            return True
        else:
            print("Queue is not empty")
            return False

    def enQueue(self, data):
        new_node = Node(data)
        if self.top is None:
            # If queue is empty, point top to the new node
            self.top = new_node
            new_node.next = self.top  # Circular link
        else:
            # Go to the last node
            temp = self.top
            while temp.next != self.top:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.top  # Make the new node point to the top (circular)

    def deQueue(self):
        if self.isEmpty():
            return None

        if self.top.next == self.top:
            # Only one node in the queue
            deq_data = self.top.data
            self.top = None
        else:
            # More than one node in the queue
            temp = self.top
            while temp.next != self.top:
                temp = temp.next
            deq_data = self.top.data
            temp.next = self.top.next
            self.top = self.top.next

        return deq_data

    def getFront(self):
        if self.isEmpty():
            return None
        return self.top.data

    def printQueue(self):
        if self.isEmpty():
            return
        temp = self.top
        queue_list = "Queue Front -> "
        while True:
            queue_list += f"{temp.data} | "
            temp = temp.next
            if temp == self.top:
                break
        print(queue_list + " -> Loop to Front")

def main():
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.printQueue()
    print(f"Dequeued: {q.deQueue()}")
    q.printQueue()
    print(f"Front of the queue: {q.getFront()}")
    print(f"Dequeued: {q.deQueue()}")
    q.printQueue()
    print(f"Dequeued: {q.deQueue()}")
    q.printQueue()
    print(f"Dequeued: {q.deQueue()}")
    q.printQueue()
    q.isEmpty()

main()

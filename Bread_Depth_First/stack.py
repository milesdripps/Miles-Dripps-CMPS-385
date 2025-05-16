class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.previous = None

class Stack:
    def __init__(self):
        self.top = None

    def insert(self, data):
        new_node = Node(data)

        if not self.top:
            self.top = new_node
        else:  # Insert item to the top of the stack
            new_node.next = self.top
            self.top = new_node

    def isempty(self):
        return self.top is None


    def top_and_pop(self):
        top = self.top

        if not top:
            return None

        top_to_pop = top.data
        if top.next:
            self.top = top.next
        else:
            self.top = None

        return top_to_pop

    def display(self):
        top = self.top
        if not top:
            print("stack empty")
            return

        stack_list = "Top ->"

        while top:
            stack_list += (f"{top.data}\n")
            top = top.next

        print(stack_list)

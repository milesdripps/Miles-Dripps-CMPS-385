# Miles Dripps, Stack implementation in CMPS 385
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def to_top(self, data):
        #add to top of stack
        add_node = Node(data)
        add_node.next = self.top
        self.top = add_node
        return 0

    def pop(self):
        #delete from top of stack
        self.top = self.top.next
        return 0

    def printstack(self):
        tmp = self.top
        stack_list = "Stack Top -> "
        while tmp:
            stack_list += f"{tmp.data} | "
            tmp = tmp.next
        print(stack_list)


def main():
    stack1 = Stack()
    stack1.to_top(data=12)
    stack1.to_top(data=10)
    stack1.to_top(data=8)
    stack1.to_top(data=1000)
    stack1.printstack()
    stack1.pop()
    stack1.printstack()
    stack1.pop()
    stack1.printstack()
    stack1.pop()
    stack1.printstack()



main()





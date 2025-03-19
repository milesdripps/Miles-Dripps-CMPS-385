# Miles Dripps
#
# CMPS 385: Min-Heap implementation

class Heap():
    def __init__(self, isMin:bool):
        self.isMin = isMin
        self.heap = []
    #Gets the parent index of a node
    def parent(self, index):
        return (index - 1) // 2

    #Gets the left child of a node
    def leftchild(self, index):
        return index * 2 + 1

    #Gets the right child of a node
    def rightchild(self, index):
        return index * 2 + 2

    #Swap two nodes
    def swapPosition(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    #For elements added at the end of the list.
    def bubbleUp(self, index):
        #bubble up to a certain index
        if self.isMin:
            while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
                self.swapPosition(index, self.parent(index))

                index = self.parent(index)
        else:
            while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
                self.swapPosition(index, self.parent(index))

                index = self.parent(index)

    def bubbleDownMinHeap(self, index):
        #Keep track of the current parent node
        parent = index

        left = self.leftchild(index)
        right = self.rightchild(index)

    #if the left or right child is less than the parent, we swap them and bubble down
        if left < len(self.heap) and self.heap[left]  < self.heap[parent]:
            parent = left

        if right < len(self.heap) and self.heap[right]  < self.heap[parent]:
            parent = right

        if parent != index:
            self.swapPosition(parent, index)
            # Recursively  bubble down
            self.bubbleDownMinHeap(parent)

    def bubbleDownMaxHeap(self, index):
        #Keep track of the current parent node
        parent = index

        left = self.leftchild(index)
        right = self.rightchild(index)

    #if the left or right child is less than the parent, we swap them and bubble down
        if left < len(self.heap) and self.heap[left] > self.heap[parent]:
            parent = left

        if right < len(self.heap) and self.heap[right] > self.heap[parent]:
            parent = right

        if parent != index:
            self.swapPosition(parent, index)
            # Recursively  bubble down
            self.bubbleDownMaxHeap(parent)

    def addNode(self, data):
        self.heap.append(data)
        self.bubbleUp(len(self.heap) - 1)
        print(f"Added {data}: {self.heap}")

    def deleteNode(self, data):
        for x in range(len(self.heap) - 1):
            if data == self.heap[x]:
                self.swapPosition(x, len(self.heap)-1)
                self.heap.pop()
                if self.isMin:
                    self.bubbleDownMinHeap(x)
                else:
                    self.bubbleDownMaxHeap(x)
                print(f"Deleted {data}: {self.heap}")
                return 0

        print(f"Could not find node {data}...")


def main():

    exampleheap = Heap(isMin=True)
    exampleheap.addNode(50)
    exampleheap.addNode(70)
    exampleheap.addNode(40)
    exampleheap.addNode(20)
    exampleheap.addNode(10)
    exampleheap.addNode(9)
    exampleheap.addNode(10)
    exampleheap.addNode(11)
    exampleheap.addNode(6)
    exampleheap.deleteNode(10)
    exampleheap.deleteNode(9)
    print("Max Heap")
    exampleMAXheap = Heap(isMin=False)
    exampleMAXheap.addNode(50)
    exampleMAXheap.addNode(40)
    exampleMAXheap.addNode(70)
    exampleMAXheap.addNode(20)
    exampleMAXheap.addNode(9)
    exampleMAXheap.addNode(61)
    exampleMAXheap.addNode(50)
    exampleMAXheap.deleteNode(10)
    exampleMAXheap.deleteNode(9)


main()

class BST:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.value:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def delete(self, data):
        if data < self.value:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.value:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_tree = self.right
            while min_tree.left:
                min_tree = min_tree.left
            self.value = min_tree.value
            self.right = self.right.delete(min_tree.value)
        return self

    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

def main():
    bst = BST(25)
    bst.insert(20)
    bst.insert(26)
    bst.insert(29)
    bst.insert(12)
    bst.insert(1)
    bst.insert(6)
    bst.insert(8)
    bst.insert(30)
    bst.pre_order()
    print("deleting")
    bst.delete(8)
    bst.pre_order()

main()

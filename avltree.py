from types import NoneType


class AVL:
    # Define base node
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height: int = 1 # Height is always 1

    def height_of_node(self, node):
        # If node does not exist, return a height of 0
        if not node:
            return 0
        print(f"height of {node.value} is {node.height} ") # for testing purposes
        # Else, return the node height
        return node.height

    def right_rotation(self, a):
        """
                        a
                      /
                     b
                    /
                    c
        """

        # Define b as the left child of node A
        b = a.left
        # A will now take b's right child as its left child
        a.left = b.right
        # B will now take A as its right child
        b.right = a

        # Update heights
        a.height = 1 + max(self.height_of_node(a.left), self.height_of_node(a.right))
        b.height = 1 + max(self.height_of_node(b.left), self.height_of_node(b.right))

        # Return new root node
        return b

    def left_rotation(self, a):
        """
                a
                   \
                        a
                            \
                             c

        """
        # B is the right child of node A
        b = a.right
        # A will take B's left child as its right child
        a.right = b.left
        # B becomes the new root by taking A as its left child
        b.left = a

        #update heights
        a.height = 1 + max(self.height_of_node(a.left), self.height_of_node(a.right))
        b.height = 1 + max(self.height_of_node(b.left), self.height_of_node(b.right))

        #Return b as the new root node
        return b

    def insert(self, value):

            # Recursively check for open spots in the tree
            if value < self.value:
                if self.left:
                    self.left = self.left.insert(value)
                else:
                    print(f"left insert {value}")
                    self.left = AVL(value) # Spot found, continue
            elif value > self.value:
                if self.right:
                    self.right = self.right.insert(value) # Insert passing in self.right as self
                else:
                    print(f"right insert {value}")
                    self.right = AVL(value) # Spot found
            else:
                return self

            # Update height of inserted node (add one since we are above the inserted node)
            self.height = 1 + max(self.height_of_node(self.left), self.height_of_node(self.right))
            balance = self.balance(self.left,self.right) # Get the balance of the current node
            print(f"balance of {self.value} is {balance}")


            # Check for imbalance and perform rotations.
            if balance > 1 and self.balance(self.left.left,self.left.right) > 0: #balance of self.left is >0, just r rotate
                print(f"{self.value} needs  R rotation")
                return self.right_rotation(self)
            if balance > 1 and self.balance(self.left.left,self.left.right) < 0: #Double rotate
                print(f"{self.value} needs LR rotation, value is {value}")
                self.left = self.left_rotation(self.left)
                return self.right_rotation(self)

            if balance < -1 and self.balance(self.right.left,self.right.right) < 0:
                print(f"{self.value} needs  L rotation")
                return self.left_rotation(self)
            if balance < -1 and self.balance(self.right.left,self.right.right) > 0: #Double rotate
                print(f"{self.value} needs  RL rotation")
                self.right = self.right_rotation(self.right)
                return self.left_rotation(self)

            #After rotatating, or no rotations needed, release stack back up to the next recursive call
            return self

    def balance(self,Lnode,Rnode):
        return self.height_of_node(Lnode) - self.height_of_node(Rnode) # Balance factor = height of left node - height of right node

    def print_tree(self):
        print(self.value)

        #Pre order printing traversal
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        else:
            return


def main():
    #remember to reassign back to tree =
    tree = AVL(10)
    tree = tree.insert(7)
    tree = tree.insert(2)
    tree = tree.insert(5)
    tree = tree.insert(9)
    tree = tree.insert(13)
    tree = tree.insert(30)
    tree = tree.insert(18)
    tree = tree.insert(15)
    print("printing tree")
    tree.print_tree()

main()

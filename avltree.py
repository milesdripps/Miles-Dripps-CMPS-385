from types import NoneType


class AVL:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height: int = 1

    def height_of_node(self, node):
        if not node:
            return 0
        print(f"height of {node.value} is {node.height} ")
        return node.height

    def right_rotation(self, a):
        """
                        a
                      /
                     b
                    /
                    c
        """

        b = a.left
        a.left = b.right

        b.right = a


        a.height = 1 + max(self.height_of_node(a.left), self.height_of_node(a.right))
        b.height = 1 + max(self.height_of_node(b.left), self.height_of_node(b.right))

        return b

    def left_rotation(self, a):
        """
                a
                   \
                        a
                            \
                             c

        """
        b = a.right
        a.right = b.left
        b.left = a


        a.height = 1 + max(self.height_of_node(a.left), self.height_of_node(a.right))
        b.height = 1 + max(self.height_of_node(b.left), self.height_of_node(b.right))

        return b

    def insert(self, value):

            # Recursively check for open spots in the tree
            if value < self.value:
                if self.left:
                    self.left = self.left.insert(value)
                else:
                    print(f"left insert {value}")
                    self.left = AVL(value)
            elif value > self.value:
                if self.right:
                    self.right = self.right.insert(value)
                else:
                    print(f"right insert {value}")
                    self.right = AVL(value)
            else:
                return self

            # Update height of inserted node (add one since we are above the inserted node)
            self.height = 1 + max(self.height_of_node(self.left), self.height_of_node(self.right))
            balance = self.balance(self.left,self.right)
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

            return self

    def balance(self,Lnode,Rnode):
        return self.height_of_node(Lnode) - self.height_of_node(Rnode)

    def print_tree(self):
        print(self.value)

        #Pre order
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        else:
            return


def main():
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

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

if __name__ == '__main__':
    root = Node('m')
    root.insert ('a')
    root.insert ('i')
    root.insert ('r')
    root.insert ('x')
    root.insert ('l')
    root.insert ('e')
    root.insert ('c')
    root.insert ('b')
    root.insert ('l')

print("In Order Transversal: ")
def inOrderPrint(tree):
    if tree is None:
        return
    else:
        inOrderPrint(tree.left)
        print(tree.data, end=" ")
        inOrderPrint(tree.right)

inOrderPrint(root)
print(" ")
print(" ")
print("Pre Order Transversal: ")
def preOrderPrint(tree):
    if tree is None:
        return
    else:
        print(tree.data, end=" ")
        preOrderPrint(tree.left)
        preOrderPrint(tree.right)

preOrderPrint(root)
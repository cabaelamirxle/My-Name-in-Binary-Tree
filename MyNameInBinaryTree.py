class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data == None:
            self.data = data
        else:
            if self.left < self.data:
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
    root.insert ('a')
    root.insert ('b')
    root.insert ('a')
    root.insert ('e')
    root.insert ('l')
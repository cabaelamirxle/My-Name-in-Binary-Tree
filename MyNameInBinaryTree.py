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
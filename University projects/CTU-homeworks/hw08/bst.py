class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 0
    def insert(self, value):
        new = Node(value)
        tmp = self.root
        if self.root is None:
            self.root = new
            return self.root.value
        while True:
            if tmp.value > new.value:
                if tmp.left is None:
                    tmp.left = new
                    return new.value
                else:
                    tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = new
                    return new.value
                else:
                    tmp = tmp.right
    def fromArray(self, array):
        for i in array:
            self.insert(i)
    def search(self, value):
        self.visited = 0
        if self.root is not None:
            tmp = self.root
            while True:
                self.visited += 1
                if value == tmp.value:
                    return True
                elif value < tmp.value:
                    if tmp.left is not None:
                        tmp = tmp.left
                    else:
                        return False
                elif value > tmp.value:
                    if tmp.right is not None:
                        tmp = tmp.right
                    else:
                        return False
        else:
            return False
    def min(self):
        self.visited = 0
        if self.root is not None:
            tmp = self.root
            self.visited += 1
            while tmp.left is not None:
                self.visited += 1
                tmp = tmp.left
            return tmp.value
        else:
            return False

    def max(self):
        self.visited = 0
        if self.root is not None:
            tmp = self.root
            self.visited += 1
            while tmp.right is not None:
                self.visited += 1
                tmp = tmp.right
            return tmp.value
        else:
            return False
    def visitedNodes(self):
        return self.visited

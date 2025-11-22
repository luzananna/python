class Node:

    def __init__(self, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def one(self, cars):
        for i in range (len(cars)):
            car = cars[i]
            dt.two(car)
        sort()

    def two(self, car):
        new_node = Node(car)
        tmp_node = self.head
        if tmp_node == None:
            self.head = new_node
            return
        while tmp_node.nextNode != None:
            tmp_node = tmp_node.nextNode
        tmp_node.nextNode = new_node
        new_node.prevNodeNode = tmp_node
        sort()

    def three(self, x, y):
        tmp_node = self.head
        while tmp_node.data.identification != x:
            tmp_node = tmp_node.nextNode
            if tmp_node == None:
                return None
        tmp_node.data.name = y

    def four(self, x, y):
        tmp_node = self.head
        while tmp_node.data.identification != x:
            tmp_node = tmp_node.nextNode
            if tmp_node == None:
                return None
        tmp_node.data.brand = y

    def five(self, x):
        tmp_node = self.head
        while tmp_node.data.identification != x:
            tmp_node = tmp_node.nextNode
            if tmp_node == None:
                return None
        tmp_node.data.active = True

    def six(self, x):
        tmp_node = self.head
        while tmp_node.data.identification != x:
            tmp_node = tmp_node.nextNode
            if tmp_node == None:
                return None
        tmp_node.data.active = False

    def seven(self):
        return self.head

    def eight(self):
        return self

    def nine(self):
        summ = 0
        tmp_node = self.head
        while tmp_node != None:
            if tmp_node.data:
             summ += tmp_node.data.price
             tmp_node = tmp_node.nextNode
        return (summ)

    def ten(self):
        self.head = None

    def eleven(self):
        for i in range (5):
            tmp_node = self.head
            while tmp_node.nextNode != None:
                if tmp_node.data.price > tmp_node.nextNode.data.price:
                    tmp_node.data, tmp_node.nextNode.data = tmp_node.nextNode.data, tmp_node.data
                tmp_node = tmp_node.nextNode

class Car:

    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

    def __str__(self):
        return f"{self.identification} {self.name} {self.brand} {self.price} {self.active}"

dt = LinkedList()


def init(cars):
    dt.one(cars)

def add(car):
    dt.two(car)

def updateName(identification, name):
    dt.three(identification, name)

def updateBrand(identification, brand):
    dt.four(identification, brand)

def activateCar(identification):
    dt.five(identification)

def deactivateCar(identification):
    dt.six(identification)

def getDatabaseHead():
    return dt.seven()
    
def getDatabase():
    return dt.eight()

def calculateCarPrice():
    return dt.nine()

def clean():
    dt.ten()

def sort():
    dt.eleven()




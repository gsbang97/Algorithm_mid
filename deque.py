class Node:
    def __init__(self,data) -> None:
        self.rlink = None
        self.llink = None
        self.data = data
        pass
    
class Deque:        
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        pass
    def isEmpty(self):
        if self.front is None or self.rear is None:
            return True
        return False
    def insertFront(self,data):
        new = Node(data)
        if self.isEmpty():
            self.front = self.rear = new
        else:
            new.rlink = self.front
            self.front.llink = new           
            self.front = new
    def insertRear(self,data):
        new = Node(data)
        if self.isEmpty():
            self.front = self.rear = new
        else:
            new.llink = self.rear
            self.rear.rlink = new           
            self.rear = new
    def deleteFront(self):
        if self.isEmpty(): 
            print("오류 발생")
            return False
        old = self.front
        self.front = self.front.rlink
        self.front.llink = None
        if self.isEmpty(): self.rear = None
        return old.data
    def deleteRear(self):
        if self.isEmpty(): 
            print("오류 발생")
            return False
        old = self.rear
        self.rear = self.rear.llink
        self.rear.rlink = None
        if self.isEmpty(): self.front = None
        return old.data
    def removeRear(self):
        if self.isEmpty(): 
            print("오류 발생")
            return False
        self.rear = self.rear.llink
        self.rear.rlink = None
        if self.isEmpty(): self.front = None
    def removeFront(self):
        if self.isEmpty(): 
            print("오류 발생")
            return False
        self.front = self.front.rlink
        self.front.llink = None
        if self.isEmpty(): self.rear = None
    def __str__(self) -> str:
        s = ""
        n = self.front
        while n is not None:
            s = s + n.data + " "
            n = n.rlink
        return s
        pass
dq = Deque()
for i in range(10):
    dq.insertFront(str(i))
print(dq)
for i in range(10):
    dq.insertRear(str(i))
print(dq)
print(dq.deleteRear())
print(dq)
print(dq.deleteFront())
print(dq)

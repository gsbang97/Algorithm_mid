class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        if self.front is None:
            return True
        return False
    def enqueue(self, data):
        new = Node(data)
        if self.isEmpty():
            self.rear = self.front = new
        else:
            self.rear.link = new
            self.rear = new
    def dequeue(self):
        if(self.isEmpty()): 
            print("오류 발생")
            return False
        old = self.front
        self.front = self.front.link
        if self.isEmpty(): self.rear = None
        return old.data
    def delete(self):
        if(self.isEmpty()): 
            print("오류 발생")
            return False
        self.front = self.front.link
    def __str__(self):
        n = self.front
        s = ""
        while n is not None:
            s = s + n.data + " "
            n = n.link
        return s
q = queue()
q.insert('a')
q.insert('b')
q.insert('c')
print(q) # a b c
print(q.pop()) # a
print(q) # b c
q.delete()
print(q) # c


        
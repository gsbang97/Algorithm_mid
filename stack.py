class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
class stack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    def insert(self, data):
        new = Node(data)
        if self.isEmpty():
            self.top = new
        else:
            new.link = self.top
            self.top = new
    def pop(self):
        if(self.isEmpty()): 
            print("오류 발생")
            return False
        old = self.top
        self.top = self.top.link
        return old.data
    def delete(self):
        if(self.isEmpty()): 
            print("오류 발생")
            return False
        self.top = self.top.link
    def __str__(self):
        n = self.top
        s = ""
        while n is not None:
            s = s + n.data + " "
            n = n.link
        return s
s = stack()
s.insert('a')
s.insert('b')
s.insert('c')
print(s) # c b a
print(s.pop()) # c
print(s) # b a
s.delete()
print(s) # a


        
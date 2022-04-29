class Node:
    def __init__(self):
        self.value =  None
        self.next =  None

class LinkedList():
    def __init__(self):
        self.head

    def append(self, x):
        novo = Node()
        novo.__value = x

        q = self.__head
        while q._next != None:
            q = q._next
        q._next = novo

    def insert(self, x, pos):
        pass

    def remove(self, x):
        novo = Node()
        novo.__value = x

        q =  self 

    def print(self):
        pass




novo = Node()
test2 = novo
novo.__value = 'x'
print(novo)
print(novo.value)


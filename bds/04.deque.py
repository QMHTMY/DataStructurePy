#!/usr/bin/python3
#python实现双端队列
#Date: 2020-07-13

class Deque:
    """双端队列"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return [] == self.items 
    
    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self, item):
        return self.items.pop()

    def removeRear(self, item):
        return self.items.pop(0)

if __name__ == "__main__":
    dq = Deque()
    dq.addFront(1)
    dq.addFront(2)
    dq.addReal(3)
    dq.addReal(4)
    print(dq.isEmpty())
    print(dq.size())
    print(dq.removeRear())

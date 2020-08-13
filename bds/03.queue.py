#!/usr/bin/python3
# python实现队列
# Date: 2020-07-13

class Queue():
    """列表实现队列"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return [] == self.items

    def size(self):
        return len(self.items)

    def isExist(self, item):
        return item in self.items

    def pickItem(self, index):
        return self.items[index]

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.isExist(0))
    print(q.pickItem(3))
    print(q.size())

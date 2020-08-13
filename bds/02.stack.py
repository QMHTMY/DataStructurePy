#!/usr/bin/python3
# python实现栈
# Date: 2020-07-13

class Stack():
    """列表组栈"""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return 0 == len(self.items)

    #def peek(self):
    #    if self.isEmpty():
    #        return None
    #    return self.items[-1]

if __name__ == "__main__":
    stk = Stack()
    stk.push(5)
    stk.push(6)
    stk.push(1)
    print('size ', stk.size())
    print('top ', stk.peek())
    print('rmtop ', stk.pop())
    print('size ', stk.size())

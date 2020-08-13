#!/usr/bin/python3
# python实现链表
# Date: 2020-07-13

class Node():
    """链表节点"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, newdata):
        self.data = newdata
    
    def getData(self):
        return self.data

    def setNext(self, newnext):
        self.next = newnext

    def getNext(self):
        return self.next

class UnorderedList():
    """未排序链表"""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return None == self.head

    def add(self, item):
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode

    def append(self, item):
        #O(n)
        current = self.head 
        previous = None
        while None != current:
            previous = current
            current = current.getNext()

        if previous == None:
            self.add(item)
        else:
            newnode = Node(item)
            newnode.setNext(None)
            previous.setNext(newnode)

    def insert(self, pos, item):
        #O(n)
        assert isinstance(pos, int), f'pos={pos} must be int'

        #1.转化pos为0到n-1
        size  = self.size() 
        pos = pos + size if pos < 0 else pos #先转化为正数

        if pos < 0:          #若仍小于0，则直接令为0
            pos = 0

        if pos >= size:      #若大于等于size，则直接令为size-1
            pos = size - 1   #若size = 0, pos = -1，错误，需要处理 

        if size == 0:        #若元素个数size为0，上一步的pos = -1
            pos = 0          #所以此处的处理必不可少，且顺序不可更改

        #2.查找到需要插入位置的元素
        previous = None
        current  = self.head 
        while pos > 0:
            previous = current 
            current = current.getNext()
            pos -= 1
        
        #3.插入元素
        if previous == None:
            self.add(item)   #size=0 或pos=0时的情况
        else:
            newnode = Node()
            newnode.setNext(current)
            previous.setNext(newnode)

    def pop(self, pos=''):
        #未输入参数默认弹出最后一个元素
        sz = self.size() 
        if pos == '':
            pos = sz - 1

        assert isinstance(pos, int), f'pos={pos} must be int'
        #转化pos为0到n-1，并判断是否超界
        posunchange = pos
        pos = pos + sz if pos < 0 else pos
        if pos < 0 or pos >= sz:
            raise ValueError(f'index {posunchange} out of range') 
        
        #按照pos，查找出所需元素
        previous = None
        current  = self.head 
        while pos > 0:
            previous = current 
            current = current.getNext()
            pos -= 1

        #设置前后连接，弹出元素
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return current.getData()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        found= False
        while None != current and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.head
        found= False
        location = 0
        while None != current and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()
                location += 1

        if found:
            return location  #位置从0开始计算
        else:
            return None

    def remove(self, item):
        current = self.head 
        found =  False
        previous = None
        while None != current and not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current  = current.getNext()
        
        if not found:
            raise ValueError(f'{item} not in chain') 

        if previous == None:
            self.head = current.getNext() 
        else:
            previous.setNext(current.getNext())

class OrderedList():
    """有序列表，保存长度变量"""
    def __init__(self):
        self.head = None 
        self.size = 0

    def isEmpty(self):
        return 0 == self.size

    def size(self):
        return self.size

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() >= item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        newnode = Node(item)
        if previous == None:
            newnode.setNext(self.head)
            self.head = newnode
        else:
            newnode.setNext(current)
            previous.setNext(newnode)

        self.size += 1

    def search(self, item):
        current = self.head
        found= False
        while None != current and not found:
            data = current.getData()
            if item < data:
                break
            elif item == data:
                found = True
            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.head
        found= False
        location = 0
        while None != current and not found:
            data = current.getData()
            if item < data:
                break
            elif item == data:
                found = True
            else:
                current = current.getNext()
                location += 1

        if found:
            return location  #位置从0开始计算
        else:
            return None

    def pop(self, pos=''):
        #未输入参数默认弹出最后一个元素
        sz = self.size() 
        if pos == '':
            pos = sz - 1

        assert isinstance(pos, int), f'pos={pos} must be int'
        
        #转化pos为0到n-1，并判断是否超界
        posunchange = pos
        pos = pos + sz if pos < 0 else pos
        if pos < 0 or pos >= sz:
            raise ValueError(f'index {posunchange} out of range') 
        
        #按照pos，查找出所需元素
        previous = None
        current  = self.head 
        while pos > 0:
            previous = current 
            current = current.getNext()
            pos -= 1

        #设置前后连接，元素数量减1，弹出元素
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1

        return current.getData()

    def remove(self, item):
        current = self.head 
        found =  False
        previous = None
        while None != current and not found:
            data = current.getData()
            if item < data:
                break
            elif item == data:
                found = True
            else:
                previous = current
                current  = current.getNext()
        
        if not found:
            raise ValueError(f'{item} not in chain') 

        if previous == None:
            self.head = current.getNext() 
        else:
            previous.setNext(current.getNext())

        self.size -= 1

if __name__ == "__main__":
   udl = UnorderedList()
   udl.add(1)
   udl.add(2)
   udl.append(4)
   udl.insert(0,3)
   print(udl.size())
   print(udl.index(2))

   odl = OrderedList()
   odl.add(9)
   odl.add(0)
   odl.add(0)
   odl.append(-1)
   odl.append(4)
   odl.insert(0,2)
   print(odl.size())
   print(odl.index(4))

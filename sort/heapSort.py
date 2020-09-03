#!/usr/bin/python3
"""堆排序
包括
从小到大的正排序，用大根堆
从大到小的逆排序，用小根堆
"""

def bigHeapSort(alist):
    """大根堆正排序"""
    bigBuildHeap(alist)                                      
    index = len(alist) - 1                               #初始化构建堆 
    while index > 0:                                                          
        alist[0], alist[index] = alist[index], alist[0]  #取出最大值                       
        percUp(alist, index, 0)                          #从0开始构建大根堆 
        index -= 1                                       #循环直到排序完成   
                                                         
    return alist

def bigBuildHeap(alist):
    #构建堆，构建后的堆满足基本有序(从大到小)
    size = len(alist)
    lastParent = (size - 1) // 2
    while lastParent > -1:  #包含0
        percUp(alist, size, lastParent)
        lastParent -= 1

def percUp(alist, size, parent):
    #尽量将大的元素往上冒
    left = 2*parent + 1
    right = 2*parent + 2

    largest = parent
    if left < size and alist[left] > alist[largest]:
        largest = left
    if right < size and alist[right] > alist[largest]:
        largest = right

    if largest != parent:
        alist[largest], alist[parent] = alist[parent], alist[largest]
        percUp(alist, size, largest)

def littleHeapSort(alist):
    """小根堆逆排序"""
    littleBuildHeap(alist)                              #初始化构建堆
    index = len(alist) - 1                                
    while index > 0:                                    
        alist[0], alist[index] = alist[index], alist[0] #取出最大值 
        percDown(alist, index, 0)                       #从0开始构建小根堆
        index -= 1                                      #循环直到排序完成  
                                                          
    return alist

def littleBuildHeap(alist):
    #构建堆，构建后的堆满足基本有序(从小到大)
    size = len(alist)
    lastParent = (size - 1) // 2
    while lastParent > -1:  #包含0
        percDown(alist, size, lastParent)
        lastParent -= 1

def percDown(alist, size, parent):
    #尽量将大的元素往下放
    left = 2*parent + 1
    right = 2*parent + 2

    minium = parent
    if left < size and alist[left] < alist[minium]:
        minium = left
    if right < size and alist[right] < alist[minium]:
        minium = right

    if minium != parent:
        alist[minium], alist[parent] = alist[parent], alist[minium]
        percDown(alist, size, minium)

class BinaryHeap():
    """二叉堆，可实现优先队列"""
    def __init__(self):
        self.heapList = [0] #0作为占位用，是为满足2p, 2p+1为p的左右子节点
        self.size = 0

    def insert(self, val):
        self.heapList.append(val)
        self.size += 1
        self.percUp(self.size)
    
    def percUp(self, index):
        #向上移动元素实现平衡
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index//2]:
                tmp = self.heapList[index//2]
                self.heapList[index//2] = self.heapList[index]
                self.heapList[index] = tmp
            index //= 2 

    def getMin(self):
        if self.size > 0:
            return self.heapList[1]
        else:
            return None
    
    def delMin(self):
        #因为0占位，最小值在index=1的位置
        if self.size > 0:
            minium = self.heapList[1]
            self.heapList[1] = self.heapList[self.size] #不能出栈，size=1时会引发IndexError
            self.heapList.pop() 
            self.size -= 1
            self.percDown(1)
        else:
            minium = None

        return minium

    def percDown(self, parent):
        #向下移动元素实现平衡
        while (2 * parent) <= self.size:
            mc = self.minChild(parent)
            if self.heapList[parent] > self.heapList[mc]:
                self.heapList[parent], self.heapList[mc] = self.heapList[mc], self.heapList[parent]
            parent = mc

    def minChild(self, parent):
        if (2 * parent + 1) > self.size: #只有左孩子
            return 2 * parent 
        else:                            #有左右孩子
            if self.heapList[2 * parent] < self.heapList[2 * parent+ 1]:
                return 2 * parent
            else:
                return 2 * parent + 1
         
    def buildHeap(self, alist):
        self.size = len(alist)
        self.heapList = [0] + alist

        lastParent = len(alist) // 2     #取中值，所有叶及子都能处理
        while lastParent > 0:
            self.percDown(lastParent)
            lastParent -= 1

        #插入元素时需要从最底层往上升
        #构建堆时需要从最后一个内部节点逐步回撤到根，同时不断将元素下降
        #遵循原则：大大取大，小小取小，有向上冒泡或下沉的感觉

    def isEmpty(self):
        return 0 == self.size

    def size(self):
        return self.size

if __name__ == "__main__":
    alist = [0,99,-1,2,9,10,8,3,5,-100]

    bhs = bigHeapSort(alist)
    print(bhs)

    lhs = littleHeapSort(alist)
    print(lhs)

    #bh = BinaryHeap()
    #for item in lst:
    #    bh.insert(item)

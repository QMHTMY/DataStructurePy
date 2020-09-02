#!/usr/bin/python3

"""选择排序
每轮循环标记出最大值位置，最后交换元素到对应位置
"""

def selectionSort1(alist):
    """修改版：从头开始"""
    if alist is None:
        return alist

    for fillslot in range(len(alist) - 1, 0, -1):
        posMax = 0
        for loc in range(1, fillslot+1):
            if alist[loc] > alist[posMax]:
                posMax = loc
        alist[fillslot], alist[posMax] = alist[posMax], alist[fillslot]

    return alist

def selectionSort2(alist):
    """修改版：从末尾开始"""
    if alist is None:
        return alist

    for fillslot in range(len(alist) - 1, 0, -1):
        posMax = fillslot 
        for i in range(fillslot):
            if alist[i] > alist[posMax]:
                posMax = i 
        alist[fillslot], alist[posMax] = alist[posMax], alist[fillslot]

    return alist

def selectionSort3(alist):
    """修改版：若已排序则提前停止"""
    if alist is None:
        return alist

    exchange = True
    fillslot = len(alist) - 1
    while fillslot > 0 and exchange:
        exchange = False
        posMax = fillslot
        for loc in range(1, fillslot+1):
            if alist[loc] > alist[posMax]:
                posMax = loc

        if posMax != fillslot: 
            alist[fillslot], alist[posMax] = alist[posMax], alist[fillslot]
            exchange = True

        fillslot -= 1
    
    return alist

if __name__ == "__main__":
    lst = [0,8,20,2,4,9,33,17,1,44,11,13,2,14,4,49,15,7,1,30,40,50]
    print(selectionSort3(lst))

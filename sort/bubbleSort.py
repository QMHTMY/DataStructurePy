#!/usr/bin/python3

"""冒泡排序
优点：维持项的稳定，缺点：费时
每轮循环不断交换元素，最后将最大值放在最后
"""

def bubbleSort1(alist):
    if alist is None:
        return alist

    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

def bubbleSort2(alist):
    """修改版1"""
    if alist is None:
        return alist

    passnum = len(alist) - 1
    while passnum > 0:
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i], alist[i+1]
        passnum -= 1

    return alist

def bubbleSort3(alist):
    """修改版2"""
    if alist is None:
        return alist

    for i in range(1, len(alist)):
        for j in range(len(alist) - i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

def bubbleSort4(alist):
    """修改版3：若已排序则提前停止"""
    if alist is None:
        return alist

    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True

        passnum -= 1

    return alist

if __name__ == "__main__":
    lst = [0,8,20,2,4,9,33,17,1,44,11,13,2,14,4,49,15,7,1,30,40,50]
    print(bubbleSort1(lst))
    print(bubbleSort2(lst))
    print(bubbleSort3(lst))
    print(bubbleSort4(lst))

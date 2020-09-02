#!/usr/bin/python3
"""插入排序
始终在开始处维持一个排序队列
"""

def insertSort(alist):
    if alist is None:
        return alist

    for index in range(1, len(alist)): 
        pos = index
        current = alist[pos]
        while pos > 0 and current < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = current

    return alist

if __name__ == "__main__":
    alist = [0,99,-1,2,9,10,8,3,5,-100]
    print(insertSort(alist))

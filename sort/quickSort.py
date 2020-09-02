#!/usr/bin/python3
"""快速排序
选择中枢点做交换
"""

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)

def partition(alist, first, last):
    #pivotVal最好选一个中间值
    pivotVal = alist[first]

    leftmark = first + 1
    rightmark = last
    while leftmark <= rightmark:
        while leftmark <= rightmark and alist[leftmark] <= pivotVal:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= pivotVal:
            rightmark -= 1

        if leftmark <= rightmark:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark

if __name__ == "__main__":
    lst = [0,99,-1,2,9,10,8,3,5,-100]
    quickSort(lst)
    print(lst)

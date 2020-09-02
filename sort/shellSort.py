#!/usr/bin/python3
"""希尔排序
   将列表分裂成若干子表再运用插入排序
"""

def shellSort1(alist):
    """插入排序单独实现"""
    def _gapInsertSort(lst, start, gap):
        for index in range(start+gap, len(lst), gap):
            pos = index
            current = lst[pos]
            while pos >= gap and current < lst[pos - gap]:
                lst[pos] = lst[pos - gap]
                pos -= gap

            lst[pos] = current
    
    gap = len(alist) // 2
    while gap > 0:
        for start in range(gap):
            _gapInsertSort(alist, start, gap)

        gap = gap // 2
        
    return alist


def shellSort2(alist):
    """插入排序不单独实现"""
    gap = len(alist) // 2
    while gap > 0:
        for start in range(gap):
            for index in range(start+gap, len(alist), gap):
                pos = index
                current = alist[pos]
                while pos >= gap and current < alist[pos - gap]:
                    alist[pos] = alist[pos - gap]
                    pos -= gap
                alist[pos] = current

        gap = gap // 2
        
    return alist

if __name__ == "__main__":
    lst = [0,99,-1,2,9,10,8,3,5,-100]
    print(shellSort1(lst))
    print(shellSort2(lst))

#!/usr/bin/python3
"""归并排序
注意处理列表不等长的情况
"""

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[i]
                j += 1
            k += 1

        while i < len(lefthalf):     #列表不等长
            alist[k] = lefthalf[i]
            i, k= i + 1, k + 1

        while j < len(righthalf):    #列表不等长
            alist[k] = righthalf[j]
            j, k= j + 1, k + 1

if __name__ == "__main__":
    lst = [0,99,-1,2,9,10,8,3,5,-100]
    mergeSort(lst)
    print(lst)

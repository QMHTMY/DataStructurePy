#!/usr/bin/python3
"""桶排序
桶排序：计数排序的改进版，将数据均匀分配到多个桶，在各桶内可用计数排序
"""

def bucketSort(alist):
    maxi, mini  = max(alist), min(alist)
    bucketNum = (maxi - mini) // len(alist) + 1            #桶的个数n，范围在1-某个合适的值

    bucketsLst = [[] for i in range(bucketNum)]            #准备n个空列表做桶
    for i in range(len(alist)):                            
        pos = (alist[i] - mini) // len(alist)              #计算数据属于哪个桶
        bucketsLst[pos].append(alist[i])                   #往对应桶放数据
    bucketsLst = [countSort(lst) for lst in bucketsLst] #利用计数排序桶中数据

    alist.clear()
    for lst in bucketsLst:
        for item in lst:                                   #迭代输出桶内已排序数据到原列表
            alist.append(item)

    return alist 

def countSort(alist):
    """计数排序"""
    if alist == []:
        return []

    cntLstLen = max(alist) + 1
    cntLst = [0] * cntLstLen
    for i in range(len(alist)):
        cntLst[alist[i]] += 1  #数据alist[i] = k就放在第k位

    alist.clear()
    for i in range(cntLstLen):
        while cntLst[i] > 0:   #将每个位置的数据k循环输出多次
            alist.append(i)        
            cntLst[i] -= 1

    return alist 

if __name__ == "__main__":
    lst = [0,19,2,9,10,8,3,5]
    print(bucketSort(lst))

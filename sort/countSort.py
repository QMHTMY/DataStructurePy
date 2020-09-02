#!/usr/bin/python3
"""计数排序(非比较排序)
因太耗内存，只适合小范围正整数排序，但速度快于任何比较排序
计数排序利用哈希表的思想，搞映射，只是值和位置数字相同的映射 x = F(x)
复杂度O(n+k)
"""
def countSort(alist):
    #[9,8,4,2,1,4,8,4,2,11] alist original
    #[0,1,2,0,3,0,0,0,2,1,0,1] cntLst 长度为11+1 = 12
    #[1,2,2,4,4,4,8,8,9,9] alist ordered

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
    print(countSort(lst))

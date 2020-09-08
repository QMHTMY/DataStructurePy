#!/usr/bin/python3
"""基数排序(非比较排序)
按低位到高位的顺序放置数据到10个桶，依次重复到最高位就排好序了
此法，需要二倍内存
"""

#辅助函数1：按位重复排序:个位，十位，百位...
def bitSort(alist, bucket, bit):
    for item in alist:
        pos = item // pow(10, bit) % 10 #计算元素所属列表位置
        bucket[pos].append(item)

#辅助函数2：将桶内元素放回lst，
#类似将[[],[],[123,426],[],[547,941]]变成 lst = [123,456,567,921]
def toList(alist, bucket):
    alist.clear()
    for lst in bucket:  
        for item in lst:
            alist.append(item)

def radixSort(alist):
    #求最大数的位数bits
    maxi = max(alist)
    bits = len(str(maxi))         
    
    #每次循环创建10个空桶用于放元素
    for bit in range(bits):
        bucket = [[] for _ in range(10)]
        bitSort(alist, bucket, bit) 
        toList(alist, bucket)

    return alist

if __name__ == "__main__":
    lst = [0,19,2,9,10,8,3,5]
    print(radixSort(lst))

#!/usr/bin/python3
"""位图排序
大量数据，状态不多，内存装不下时的排序法
读取完基本就排序完了，非常类似计数排序，但是使用byte位而非数字位(32byte)
复杂度：O(n)
"""
class BitMap():
    def __init__(self, maxVal):
        self.size = self.elemIndex(maxVal, up=True)
        self.array = [0] * (self.size + 1)

    def elemIndex(self, num, up=False):
        """计算在数组中的索引"""
        if up:
            return (num + 31 - 1) // 31 #向上取整
        else:
            return num // 31

    def byteIndex(self, num):
        """计算在数组元素中的位索引"""
        return num % 31

    def setByte(self, num):
        elemIdx = self.elemIndex(num, up=True)
        byteIdx = self.byteIndex(num)
        self.array[elemIdx] |= (1 << byteIdx) #或操作

if __name__ == "__main__":
    bmp = BitMap(80)
    bmp.setByte(1)
    bmp.setByte(70)
    bmp.setByte(69)
    bmp.setByte(50)
    print(bmp.array)

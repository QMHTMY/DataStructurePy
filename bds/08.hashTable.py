#!/usr/bin/python3
# python实现哈希表
# Date: 2020-07-13

"""哈希算法有多种实现
   1.求余数作为位置参数 H(item) = item % length
    a.冲突解决 (开放寻址，链表，分组求和，平方取中，ascii求和，ascii取中)
    b.ascii求和冲突，字符串顺序无关，解决：添加权重
    哈希表，负载因子L越大越费时，O(L)
   2.梅森素数求余数作为位置参数 H(item) = item % hashMn
"""
class HashTable:
    def __init__(self, size=10):
        self.size  = size
        self.slots = [None] * self.size
        self.data  = [None] * self.size

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def get(self, key):
        startslot = self.hashcalc(key, self.size)

        data = None
        stop = False
        found = False
        pos = startslot
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, self.size)
                if pos == startslot:
                    stop = True
        return data

    def put(self, key, data):
        hashvalue = self.hashcalc(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, self.size)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #替换

    def hashcalc(self, key, size):
        return ord(key) % size

    def hashcalcMn(self, key, size):
        return ord(key) % 127                  #127为梅森素数

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size 

if __name__ == "__main__":
    ht  = HashTable()
    ht.put('a',1)
    ht.put('c',3)
    ht.put('d',2)
    ht.put('b',0)
    ht.put('e',4)
    print(ht.get('a'))
    ht['a'] = 4
    print(ht['a'])

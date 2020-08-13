#!/usr/bin/python3
# python实现集合
# Date: 2020-07-13

class Set:
    """列表实现集合"""
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def clear(self):
        self.items = []

    def discard(self, item):
        if item in self.items:
            self.items.remove(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError(f"Remove {item} from empty set")

    def pop(self):
        if len(self.items) != 0:
            item = self.items[0]
            self.items = self.items[1:]
        else:
            raise KeyError(f"Pop from empty set")

        return item

if __name__ == "__main__":
    s = Set()
    s.add(1)
    s.add(10)
    s.add(100)
    print(s.pop())

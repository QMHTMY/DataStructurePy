#!/usr/bin/python3
# python实现字典索树
# Date: 2020-07-13

from collections import defaultdict
class TrieNode:
    """字典树节点"""
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for s in word:
            node = node.children[s]
        node.isWord = True

    def isPrefix(self, word):
        node = self.root 
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False

        return True

    def search(self, word):
        node = self.root 
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False

        return node.isWord

if __name__ == "__main__":
    trie = Trie()
    trie.insert('apple')
    trie.insert('arm')
    trie.insert('tencent')
    trie.insert('alibaba')
    trie.insert('huawei')
    trie.insert('google')

    print(trie.search('Arm'))
    print(trie.search('arm'))
    print(trie.isPrefix('ar'))

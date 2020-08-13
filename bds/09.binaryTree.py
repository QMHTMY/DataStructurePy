#!/usr/bin/python3
# python实现二叉树
# Date: 2020-07-13

class BinaryTree:
    """ 二叉树 """
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if isinstance(newNode, BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.leftChild is not None:
            t.left = self.leftChild

        self.leftChild = t

    def insertRight(self,newNode):
        if isinstance(newNode,BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.rightChild is not None:
            t.right = self.rightChild

        self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, key):
        self.key = key

    def getRootVal(self):
        return self.key

    #内部遍历
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

#外部遍历
def preorder(tree):
    if tree != None:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRigthChild())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        print(tree.getRootVal())
        postorder(tree.getLeftChild())
        postorder(tree.getRigthChild())

#给表达式添加括号
def printexp1(tree):
    if tree.leftChild:
        print('(', end=' ')
        printexp(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printexp(tree.getRightChild())
        print(')', end=' ')

def printexp2(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

#计算表达式
import operator
def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

#计算树高度
def height(tree):
    if tree == None:
        return -1
    else:
        return 1 + max(height(tree.leftChild),height(tree.rightChild))

if __name__ == '__main__':
    t = BinaryTree(7)
    t.insertLeft(3)
    t.insertRight(9)
    inorder(t)
    x = BinaryTree('*')
    x.insertLeft('+')
    l = x.getLeftChild()
    l.insertLeft(4)
    l.insertRight(5)
    x.insertRight(7)
    print(printexp(x))
    print(postordereval(x))
    print(height(x))

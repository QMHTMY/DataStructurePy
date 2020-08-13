#!/usr/bin/python3
#python实现图
#Date: 2020-07-13

class Vertex:
    """点"""
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = 9223372036854775807 #这是sys.maxsize值，此处避免调用包
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

class Graph:
    """图"""
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    #边
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())
                
if __name__ == '__main__':
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addVertex(7)
    g.addVertex(8)

    g.addEdge(1,2,1)
    g.addEdge(1,3,1)
    g.addEdge(2,3,1)
    g.addEdge(2,5,1)
    g.addEdge(3,4,1)
    g.addEdge(4,6,1)
    g.addEdge(5,6,1)
    g.addEdge(5,7,1)
    g.addEdge(6,8,1)
    g.addEdge(7,8,1)

    print(g.getVertices())

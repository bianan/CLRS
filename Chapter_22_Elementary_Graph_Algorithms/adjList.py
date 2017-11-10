# adjacency list representation of a graph

# import unittest


class Node(object):
    def __init__(self, id):
        self.id = id # id is a char or integer
        self.connectedTo = {} # nbr: weight (notice that
        # nbr is a Node object.
        
    def addNeighbor(self, nbr, weight = 1):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + " is connected to: " + \
            str([x.id for x in self.connectedTo.keys()])
            
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def getNeighbors(self):
        return self.connectedTo.keys()
    
    
class UndirectedGraph(object):
    def __init__(self):
        self.numNodes = 0
        self.nodesDict = {} # id: node
        
    def addNode(self, node_id):
        self.numNodes += 1
        new_node = Node(node_id)
        self.nodesDict[node_id] = new_node
        return new_node
    
    def getNode(self, node_id):
        if node_id in self.nodesDict:
            return self.nodesDict[node_id]
        else:
            return None
        
    def addEdge(self, id1, id2, weight=1): # default is equal weight
        if id1 not in self.nodesDict:
            self.addNode(id1)
        if id2 not in self.nodesDict:
            self.addNode(id2)
            
        self.nodesDict[id1].addNeighbor(self.nodesDict[id2], weight)
        self.nodesDict[id2].addNeighbor(self.nodesDict[id1], weight)
        
    def getNodesId(self):
        return self.nodesDict.keys()
    
    def __contains__(self, id):
        return id in self.nodesDict
    
    def __str__(self):   # print nodes and edges in graph
        
        
        if 0 == self.numNodes:
            return "empty."
        else:
            msg = ""
            for node in self.nodesDict.values():
                msg += (str(node) + '\n')
            return msg
            
    
    
if __name__ == "__main__":
    
#     node1 = Node('s')
#     node2 = Node('r')
#
#     node1.addNeighbor(node2, 1)
#
#     print(str(node1)
    
    G = UndirectedGraph()
    G.addEdge('s', 'r')
    G.addEdge('r', 'v')
    G.addEdge('s', 'w')
    G.addEdge('w', 't')
    G.addEdge('w', 'x')
    G.addEdge('x', 't')
    G.addEdge('u', 't')
    G.addEdge('x', 'u')
    G.addEdge('x', 'y')
    G.addEdge('u', 'y')
    print(str(G))
     
    
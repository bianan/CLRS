import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import unittest
from  adjList import *
from queue import Queue
from math import inf, nan

class NodeInfo(object):
    def __init__(self, id, color = 'white', dist = inf, pre = None):
        self.id = id;
        self.color = color;
        self.dist = dist;
        self.pre = pre;
        
    def __str__(self):
        msg = str(self.id) + ' is in: color-' + str (self.color) + \
        ' dist-' + str (self.dist) + ' pre-';
        if None == self.pre:
            return msg + str(None) + '\n';
        else:
            return msg + str(self.pre.id) + '\n';

def BFS(G, src_id):
    """
    src_id:  source node id
    """
    
    
    q = Queue()

    nodes_info = {} # id: NodeInfo
    for id in G.getNodesId():
        nodes_info[id] = NodeInfo(id);
        print(str(nodes_info[id]))
        
    nodes_info[src_id].color = 'gray'
    nodes_info[src_id].dist = 0
    nodes_info[src_id].pre = None
    
    print('source node ',str(nodes_info[src_id] ))
    
    q.put(G.getNode( src_id ))
    
    while not q.empty():
        u = q.get()
        print ('visiting ', u.getId())
        
        for nbr in u.getNeighbors():
            if 'white' == nodes_info[nbr.id].color:
                nodes_info[nbr.id].color = 'gray'
                nodes_info[nbr.id].dist = nodes_info[u.id].dist +  1
                nodes_info[nbr.id].pre = u;
                q.put(nbr)
                
            nodes_info[u.id].color = 'black';
    
    print('after BFS, nodes info is: ')
    
    for info in nodes_info.values():
        print(str(info) )
        
        
    return nodes_info

def print_path(nodes_info, s, v):
    """
    s, v are ids
     """
    if v == s:
         print (s)
    elif nodes_info[v].pre == None:
        print ( 'no path from ', s, ' to ', v )
    else:
         print_path(nodes_info, s, nodes_info[v].pre.id)
         print(v)
    
     

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
    
    a = BFS(G, 's')
    print_path(a, 's', 'x')
    
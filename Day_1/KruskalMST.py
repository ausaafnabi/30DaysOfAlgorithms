from collections import defaultdict
import random


'''
Graph Class with Kruskal Minimum Spanning Tree Algorithm
'''
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [] # default dict
    
    # function to add edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    # function to union two sets
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)

        if rank[xroot] <rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] >rank[yroot]:
            parent[yroot] = xroot

        #if rank are same, then make one as root
        # and increment its rank one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    # Function to construct MST using Kruskal's algorithms 
    def KruskalMST(self):
        result = [] # result to store the MST
        i=0     # index variable for sorted edge
        e=0     # index variable for result[]
        
        # Sort all the edges in increasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        # Number of edges to be taken is equal to V-1
        while e <self.V-1:
            #Pick smallest edge and move the iteration
            u,v,w = self.graph[i]
            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)
            
            # If including this edge does'nt cause cycle,
            # indlude it in result and inc. the index of result
            if x!=y:
                e = e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
            # Discard the edge otherwise

            minimumCost = 0
            print("Edges in the constructed MST")
            for u,v, weight in result:
                minimumCost += weight
                print("%d -- %d == %d" % (u,v,weight))
            print("Minimum Spanning Tree", minimumCost)

def main():
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.KruskalMST()

if __name__ == "__main__":
    main()


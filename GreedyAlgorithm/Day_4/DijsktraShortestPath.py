import sys

maxint = 3200

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for now in range(vertices)]
        
    def printSolution(self,dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node,"\t", dist[node])
    
    # Utility function to find the vertex with minimum
    # distance value.
    def minDistance(self,dist,sptSet):

        #Initialize minimum distance for next node
        min = maxint 

        # Search not nearest vertex not in the SPT
        # (Shortest Path Tree)
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        
        return min_index
    
    #Function to implement Dijkstra
    def dijkstra(self,src):
        dist = [maxint] * self.V
        dist[src] = 0
        sptSet = [False]* self.V

        for count in range(self.V):
            # Pick the minimum distance vertex
            # from unprocessed vertices
            u = self.minDistance(dist ,sptSet)
            sptSet[u] = True
            # Update dist value of the adj vertices
            # only if curr >  new dist and c not in SPT
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [ [0,4,0,0,0,0,0,8,0],
                [4,0,8,0,0,0,0,11,0],
                [0,8,0,7,0,4,0,0,2],
                [0,0,7,0,9,14,0,0,0],
                [0,0,0,9,0,10,0,0,0],
                [0,0,4,14,10,0,2,0,0],
                [0,0,0,0,0,2,0,1,6],
                [8,11,0,0,0,0,1,0,7],
                [0,0,2,0,0,0,6,7,0],
              ]
    g.dijkstra(0);



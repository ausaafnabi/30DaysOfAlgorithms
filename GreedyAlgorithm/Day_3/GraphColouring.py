

class Graph:
    def __init__(self,edges,N):
        self.adj = [[] for _ in range(N)]
        # add edges to undirected graph
        for (src,dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def colorGraph(graph,colors,N):
    # stores color assigned to each V
    result = {}
    
    # assign color to V one by one
    for u in range(N):
        # set to store color of adj vertices of u
        # check color of adj of u and store in set
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
        #assigns vertex u the first available color
        result[u] = color
    
    for v in range(N):
        print("Color assigned to vertex",v,"is",colors[result[v]])

def main():
    colors = ["","BLUE","GREEN","BLACK","RED","WHITE","YELLOW","VIOLET","PINK","PURPLE","ORANGE"]
    edges = [(0,1),(0,4),(0,5),(4,5),(1,4),(1,3),(2,3),(2,4)]
    N = 6

    graph = Graph(edges,N)
    colorGraph(graph,colors,N)

if __name__ == "__main__":
    main()


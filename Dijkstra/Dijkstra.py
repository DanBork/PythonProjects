import sys


class Graph:    # class representing a graph
    def __init__(self, vertices):
        self.vertices = vertices    # graphs vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]    # weighted connections of each vertex

    def print_shortest_path(self, dist):    # function printing the shortest distance to each vertex
        print("Destination:     Shortest Path:")
        for node in range(self.vertices):
            print("     ",node, "               ", dist[node])

    def shortest_distance(self, dist, sptSet):  # function finding the lowest weighted path,
                                                # from vertices not included in the shortest path tree
        min_dist = sys.maxsize  # initialising distance as 'infinite'
        for i in range(self.vertices):      # reading distance (weight) of unchecked neighbours
            if dist[i] < min_dist and sptSet[i] == False:
                min_dist = dist[i]
                min_index = i

        return min_index

    def dijkstra(self, source): # Dijkstra algorithm implementation
        dist = [sys.maxsize]*self.vertices  # initialising all weights as infinite
        dist[source] = 0    # setting distance to source as 0
        sptSet = [0]*self.vertices  # initialising the shortest path tree

        for i in range(self.vertices):  # for each vertex
            x = self.shortest_distance(dist, sptSet)    # picking the minimum distance vertex

            sptSet[x]=1 # marking vertex as checked

            for y in range(self.vertices):  # update dist values of neighbours, if the current distance is greater
                                            # and the vertex is not yet checked
                if self.graph[x][y] > 0 and sptSet[y]==0 and dist[y]>dist[x]+self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]


        self.print_shortest_path(dist)


g=Graph(5)  # example graph
g.graph=[[0, 2, 0 ,0, 3],   #
       [2,0,5,1,0],         # distance to each, connected vertex
         [0,5,0,4,7],       # 0 - unconnected or itself
         [0,1,4,0,9],       # other value - weight
         [3,0,7,9,0]]       #

g.dijkstra(2)       # calculating shortest path to each node, setting the node '2' as starting point





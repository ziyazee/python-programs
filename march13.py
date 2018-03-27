'''from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        print("added",self.graph[u],u,v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            #print(self.graph[s])
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s,"=>popped")

            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
               # print(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
           # print("next round")


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(2, 1)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)

# This code is contributed by Neelam Yadav


# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v,"=>visited")

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
        print("next round")

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 4)




print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
'''

# program to find a mother vertex in O(V+E) time
from collections import defaultdict


# This class represents a directed graph using adjacency list
# representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary

    # A recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        print(v)
        print(visited[v])

        visited[v] = True
        print(v,"beacame",visited[v])
        j=0
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            print("inside i=",i)
            if visited[i] == False:
                self.DFSUtil(i, visited)



    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):

        # visited[] is used for DFS. Initially all are
        # initialized as not visited
        visited = [False] * (self.V)
       # print(" ".join(int(visited)))

        # To store last finished vertex (or mother vertex)
        v = 0

        # Do a DFS traversal and find the last finished
        # vertex
        for i in range(self.V):
            print("i=",i)
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i
                print(i)
            print("exit main loop")

        # If there exist mother vertex (or vetices) in given
        # graph, then v must be one (or one of them)

        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False] * (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v


# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(6, 5)
g.addEdge(5, 2)
g.addEdge(6, 0)
print("A mother vertex is " + str(g.findMother()))

# This code is contributed by Neelam Yadav













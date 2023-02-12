# Edge List, show connect: 0 connected to 2, 2 to 3 ...
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List, index of the array is the value of the actual  Graph node
graph_adj = [[2], [2, 3], [0,1,3], [1, 2]]

# Adjcacent Matrix

class Graph:

    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def __str__(self):
        return str(self.__dict__)

    def addVertex(self, node):
        if node in self.adjacentlist:
            print('Node already exists')
        else:
            self.adjacentlist[node] = []
            self.numberofnodes += 1


    def addEdge(self, node1, node2):
        # Undirected graph
        if node1 in self.adjacentlist and node2 in self.adjacentlist:
            self.adjacentlist[node1].append(node2)
            self.adjacentlist[node2].append(node1)

    def showConnection(self):
        for vertex, neighbors in self.adjacentlist.items():
            print(vertex, end='-->')
            print(' '.join(neighbors))



myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.showConnection()

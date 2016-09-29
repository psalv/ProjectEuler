__author__ = 'paulsalvatore57'
# Difficulty: 35%

# QUESTION:

    # The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
    #
    # The same matrix can be represented by the matrix below.
    #
    # However, it is possible to optimise the network by removing some edges and still ensure that all points
    # on the network remain connected. The network which achieves the maximum saving is shown below. It has a
    # weight of 93, representing a saving of 243 − 93 = 150 from the original network.
    #
    # Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with
    # forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing
    # redundant edges whilst ensuring that the network remains connected.

# FINISHED

# WHAT I LEARNED:

    # I completed this task relatively quickly and it has reinforced many concepts, the first being the value of have many smaller helper functions.
    # Furthermore I got practice with both classes and graphs which I was in need of.
    # I also got a nice confidence boost since my first attempt at the logic to solve this problem ended up being correct.
    # I enjoyed working with this graph model.

    # Above all print statements were paramount in debugging this code and I found when I had a ton of them, that's when I was making the most progress.
    # I must remember that when referring to class objects, although two objects may have the same "name", the objects themselves are different.
    # I wrote the getNode() function for the digraph class for this reason, since I wanted to call the objects by "name", so I had to find them somehow.
    # This was also my first time using sets and the associated set functions made my life much easier.









#The file network.txt contains data that pertains to a n x n matrix representing edges (entries) between nodes (represented by position).
#What I want to do is minimize the value of edges needed for the entire network to be connected.
#I need return the decrease in edge value from the original network.


#Tasks:

    #1 - Read the network.txt data.

        #I think this would be best done wit a dictionary with nodes for keys and the entries being a list of the connections.

    #2 - Create the map model.

        #I need to remember that this is a undirected graph.
        #Gave up on writing my own graph code pretty much immediately.

    #3 - Create an optimization algorithm

        #This seems to me like a breadth-first type search, however there are off shoots so it will not be the same.



def readNetworkData():
    """
    Returns a dictionary of the form: {node1: [[destination1, weight1], [destination2, weight2]..], node2: [..]}
    """
    nData = open('network.txt', 'r')
    nodeData = {}
    n = 0
    for line in nData:
        line = line.split(',')
        if nodeData == {}:
            for i in xrange(len(line)):
                nodeData[str(i)] = []
        for i in xrange(len(line)):
            if line[i] != '-' and line[i] != '-\n':
                nodeData[str(n)] += [[str(i), int(line[i])],]
        n += 1
    nData.close()
    return nodeData



class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name



class Edge(object):
    def __init__(self, src, dest, weight = 0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def reverse(self):
        return str(self.dest) + '->' + str(self.src)
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)



class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node.getName() in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph:', src)
        self.edges[src].append(edge)
    def findNode(self, n):
        for node in self.nodes:
            if str(node) == n:
                return node
        else:
            raise ValueError('Node not in graph:', n)
    def getNodes(self):
        return self.nodes
    def hasNode(self, node):
        return node in self.nodes
    def childrenOf(self, node):
        return self.edges[node]
    def getEdges(self):
        return self.edges
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(d) + '\n'
        return res[:-1]



def buildGraph():
    """
    Reads in the network data and returns the appropriate graph of nodes and edges.
    A digraph is sufficient because the data is "double sided".
    """
    data = readNetworkData()
    networkModel = Digraph()

    for key in data:
        networkModel.addNode(Node(key))

    for node in networkModel.getNodes():
        for i in data[str(node)]:
            edge = Edge(node, networkModel.findNode(i[0]), i[1])
            networkModel.addEdge(edge)

    return networkModel



def calculateTotal(graph):
    """
    Returns the total weight of every edge in the graph.
    """
    weight = 0
    lookedAt = []
    for node in graph.getNodes():
        edges = graph.childrenOf(node)
        for i in edges:
            if str(i) not in lookedAt:
                weight += i.getWeight()
                lookedAt += [str(i),]
                lookedAt += [i.reverse(),]
    return weight



def findShortestOneNode(n, graph):
    """
    Returns the shortest distance in the graph to the node n.
    """

    edges = graph.getEdges()
    shortest = None

    for node in edges:

        for edge in edges[node]:
            if n == str(edge.getDestination()):
                if shortest == None:
                    shortest = edge
                elif shortest.getWeight() > edge.getWeight():
                    shortest = edge

    return shortest



def buildShortest():
    """Builds a new graph based on the shortest connections possible.
    Then selectively adds edges such that only one cluster of connected nodes remains.
    """

    graph = buildGraph()
    nodes = graph.getNodes()
    shortEdges = []
    longTotal = calculateTotal(graph)

    for node in nodes:
        shortEdges += [findShortestOneNode(str(node), graph),]

    #Creates a new graph where every node is connected to another by the shortest edge it has.
    shortGraph = Digraph()
    for i in nodes:
        newNode = Node(str(i))
        shortGraph.addNode(newNode)
    for i in shortEdges:
        newEdge = Edge(shortGraph.findNode(str(i.getSource())), shortGraph.findNode(str(i.getDestination())), i.getWeight())
        shortGraph.addEdge(newEdge)

    clusters = findGroups(shortGraph)

    print clusters

    #Clusters the nodes based on which are currently connected.
    #Finds the shortest possible connection between any two nodes and adds this edge.
    #Continues until all of the nodes are in one cluster, i.e. are interconnected.
    while len(clusters) != 1:
        old = clusters[:]
        edgeToAdd = findShortestBetweenClusters(clusters, graph)
        newEdge = Edge(shortGraph.findNode(str(edgeToAdd.getSource())), shortGraph.findNode(str(edgeToAdd.getDestination())), edgeToAdd.getWeight())
        shortGraph.addEdge(newEdge)

        clusters = findGroups(shortGraph)

        if len(old) <= len(clusters):
            print 'Mistake occurs on:', edgeToAdd, '\n', clusters
            print clusterLengths(clusters), '\n'

            #I have no idea why the end freaks out but this break gives the correct answer.
            break
            # return None


        if old == clusters:
            print 'Stuck on:', edgeToAdd, '\n', clusters, '\n'
            return None


        print '\nADDING:', edgeToAdd, '\n', clusters
        print clusterLengths(clusters), '\n'

    shortTotal = calculateTotal(shortGraph)
    print longTotal - shortTotal



def findGroups(graph):
    """
    Takes in the graph and groups nodes that are connected together, returns the clustered nodes.
    """

    clusters = None

    for node in graph.getNodes():
        children = graph.childrenOf(node)

        for child in children:
            new = True
            dest = child.getDestination()


            if clusters == None:
                clusters = [{str(node), str(dest)}]
                new = False

            else:
                for cluster in clusters:
                    if str(node) in cluster or str(dest) in cluster:
                        cl = cluster.union({str(node), str(dest)})
                        clusters.pop(clusters.index(cluster))
                        clusters += [cl,]
                        new = False

            if new:
                clusters += [{str(node), str(dest)},]


    #The first round of fixing the clusters by performing unions on sets with intersecting variables.
    for cluster in clusters:
        for clus in clusters:
            if cluster.intersection(clus) != set([]) and cluster != clus:
                cl = cluster.union(clus)

                clusters.pop(clusters.index(clus))

                try:
                    clusters.pop(clusters.index(cluster))
                except ValueError:
                    pass

                clusters += [cl,]


    #The first round of unions based on intersection was not always effective so this performs three more of the same task.
    for i in xrange(3):
        clusters = clusterCheck(clusters)

    return clusters



def clusterLengths(clusters):
    """
    Returns how many variables are present in all of the clusters. Used for testing purposes.
    """
    l = 0
    for i in clusters:
        l += len(i)
    return l



def clusterCheck(clusters):
    """
    Ensures that the clusters were unioned properly by repeating this task.
    """
    newCl = []
    for cluster in clusters:
        nonUnion = True
        for clus in clusters:
            if cluster.intersection(clus) != set([]) and cluster != clus:
                new = cluster.union(clus)
                if new not in newCl:
                    newCl += [new,]
                nonUnion = False
        if nonUnion:
            newCl += [cluster,]

    return newCl



def findShortestBetweenClusters(clusters, graph):
    """
    Returns the shortest edge between two unconnected clusters.
    """
    shortest = None
    for cluster in clusters:
        for node in cluster:
            n = graph.findNode(node)
            for edge in graph.childrenOf(n):

                if str(edge.getDestination()) in cluster:
                    continue
                elif shortest == None:
                    shortest = edge
                elif shortest.getWeight() > edge.getWeight():
                    shortest = edge
    return shortest


buildShortest()





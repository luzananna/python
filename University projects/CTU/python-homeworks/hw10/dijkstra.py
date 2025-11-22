class Vertex:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None
        self.visited = False

class Edge:

    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Dijkstra:

    def __init__(self):
        self.vertexes = []


    def createGraph(self, vertexes, edgesToVertexes):
        for i in vertexes:
                for j in edgesToVertexes:
                    if i.id == j.source:
                        i.edges.append(j)
                self.vertexes.append(i)

    def computePath(self, sourceId):
        source = self.vertexes[sourceId]
        source.minDistance = 0
        vertexes = set(self.vertexes)
        while vertexes:
            currentVertex = min(vertexes, key=lambda vertex: vertex.minDistance)
            vertexes.remove(currentVertex)
            for edge in currentVertex.edges:
                target = self.vertexes[edge.target]
                newDistance = currentVertex.minDistance + edge.weight
                if newDistance < target.minDistance:
                    target.minDistance = newDistance
                    target.previousVertex = currentVertex

    def getShortestPathTo(self, targetId):
        tmp_Vertex = None
        shortestPath = []
        for vertex in self.vertexes:
            if vertex.id == targetId:
                tmp_Vertex = vertex
                break

        while True:
            shortestPath.insert(0, tmp_Vertex)
            if (tmp_Vertex.previousVertex is not None):
                tmp_Vertex = tmp_Vertex.previousVertex
            else:
                break
        return shortestPath

    def createGraph(self, vertexes, edgesToVertexes):
        for i in vertexes:
            for j in edgesToVertexes:
                if i.id == j.source:
                    i.edges.append(j)
            self.vertexes.append(i)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None
            vertex.visited = False

    def getVertexes(self):
        getvertexes = []
        for vertex in self.vertexes:
            if len(vertex.edges) > 0:
                getvertexes.append(vertex)
        return getvertexes

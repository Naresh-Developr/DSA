class Graph:
    
    def __init__(self):
        self.graph = {}

    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.vertex = self.graph[vertex] = []

    def AddEdge(self,vertex1,vertex2,isdirected = False): # isdirect represents unidirectional 
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if  not isdirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key,value in self.graph.items():
            print(f"{key} ==> {value}")

    def removeVertix(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]

            for key,value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
    
    def removeEdge(self,vertex1,vertex2):
        if self.IsEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)



    def IsEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex1] or vertex2 in self.graph[vertex2]


    def DfsTraversal(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end =' ')

            for child in self.graph[start]:
                self.DfsTraversal(child,AlreadyVisited)


    def BfsTraversal(self,start):
        AlreadyVisited={start}
        queue = [start]

        while len(queue)>0:
            s = queue.pop(0)
            print(s,end=' ')

            for child in self.graph[s]:
                if child not in AlreadyVisited:
                    AlreadyVisited.add(child)
                    queue.append(child)

    def ShortestPath(self,start,end):
        AlreadyVisited={start}
        queue = [(start,[start])]

        while len(queue)>0:
            s,path = queue.pop(0)
            #print(s,end=' ')

            for child in self.graph[s]:
                if child == end:
                    return path+[child] 
                if child not in AlreadyVisited:
                    AlreadyVisited.add(child)
                    queue.append(((child),path+([child])))


             





g = Graph()
g.AddEdge('a','b')
g.AddEdge('b','c')
g.AddEdge('b','d')
g.AddEdge('c','d')
g.display()
#g.removeVertix('c')
#g.removeEdge('a','b')
#g.display()
#g.BfsTraversal('a')
print(g.ShortestPath('a','d'))
from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v) -> None:
        self.graph[u].append(v)

    def DFS(self, u):
        visited = set()
        k = self.graph.keys()
        for i in k:
            if i not in visited:
                self.DFSUtils(i, visited)

    def DFSUtils(self, u, visited):
        visited.add(u)
        print(u, end=', ')
        for j in self.graph[u]:
            if j not in visited:
                self.DFSUtils(j, visited)

    def BFS(self, u):
        q = []
        visited = [False]*len(self.graph.keys())
        q.append(u)
        visited[u] = True
        while len(q):
            v = q.pop(0)
            print(v, end=', ')
            for i in self.graph[v]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)

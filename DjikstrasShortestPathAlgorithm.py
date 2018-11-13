import sys
import queue

inf = int(1e10)

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = []

class Graph:
    def __init__(self, nv):
        self.verts = {}
        self.nv = nv

    def addVertex(self, v):
        self.verts[v.name] = v

    def addEdge(self, src, dest, wt):
        v = self.verts[src]
        edge = [dest, wt]
        v.adj.append(edge)

    def shortestPath(self, src, dest):
        q = queue.PriorityQueue()
        q.put([0, src])
        d = [inf] * (self.nv + 1)
        d[src] = 0
        while not q.empty():
            e = q.get()
            vname = e[1]
            if vname == dest:
                return e[0]
            for nedge in self.verts[vname].adj:
                nvert, newt = nedge[0], nedge[1]
                if d[nvert] > d[vname] + newt:
                    d[nvert] = d[vname] + newt
                    q.put([d[nvert], nvert])
        return inf

def main():
    nv, ne = map(int, f.readline().split())
    g = Graph(nv)
    for name in range(1, nv + 1):
        v = Vertex(name)
        g.addVertex(v)

    for e in range(ne):
        src, dest, wt = map(int, f.readline().split())
        g.addEdge(src, dest, wt)

    src, dest = map(int, f.readline().split())

    print(g.shortestPath(src, dest))


if __name__ == "__main__":
    main()

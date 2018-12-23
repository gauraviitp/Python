import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Edge:
    def __init__(self, u, v, cap):
        self.u, self.v, self.cap = u, v, cap
        self.flow = 0


class Dinic:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.vemap = [[] for i in range(n + 1)]
        self.dist = [n + 1] * (n + 1)
        self.pt = [0] * (n + 1)

    def addEdge(self, u, v, cap):
        self.edges.append(Edge(u, v, cap))
        self.vemap[u].append(len(self.edges) - 1)
        self.edges.append(Edge(v, u, 0))
        self.vemap[v].append(len(self.edges) - 1)

    def bfs(self, s, t):
        q = [s]
        for i in range(self.n + 1):
            self.dist[i] = self.n + 1
        self.dist[s] = 0
        while (len(q) > 0):
            u = q.pop(0)
            if u == t:
                break
            for eno in self.vemap[u]:
                e = self.edges[eno]
                if e.flow < e.cap and self.dist[e.v] > self.dist[e.u] + 1:
                    self.dist[e.v] = self.dist[e.u] + 1
                    q.append(e.v)
        return self.dist[t] != self.n + 1

    def dfs(self, u, t, flow = -1):
        if u == t or flow == 0:
            return flow
        for i in range(self.pt[u], len(self.vemap[u])):
            eno = self.vemap[u][i]
            e = self.edges[eno]
            eopp = self.edges[eno ^ 1]
            if self.dist[e.u] + 1 == self.dist[e.v]:
                amount = e.cap - e.flow
                if flow != -1 and amount > flow:
                    amount = flow
                pushed = self.dfs(e.v, t, amount)
                if pushed > 0:
                    e.flow += pushed
                    eopp.flow -= pushed
                    return pushed
            self.pt[u] += 1
        return 0

    def maxFlow(self, s, t):
        total = 0
        while self.bfs(s, t):
            for i in range(self.n + 1):
                self.pt[i] = 0
            while True:
                flow = self.dfs(s, t)
                if flow == 0:
                    break
                total += flow
        return total

def main():
    n, m = map(int, f.readline().split())
    dinic = Dinic(n)
    for i in range(m):
        a, b, c = map(int, f.readline().split())
        dinic.addEdge(a, b, c)
        dinic.addEdge(b, a, c)
    total = dinic.maxFlow(1, n)
    print(total)

if __name__ == '__main__':
    main()

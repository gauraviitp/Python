import sys
import queue

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Node:

    def __init__(self, data):
        self.data = data
        self.adjacent = []

class Graph:

    def __init__(self):
        self.nodes = {}

    def addEdge(self, source, dest):
        s = self.nodes[source]
        d = self.nodes[dest]
        s.adjacent.append(d)

    def visit(self, node):
        o.write(str(node.data) + ' ')

    def bfs(self, node, s):
        if node not in s:
            q = queue.Queue()
            q.put(node)
            while not q.empty():
                cn = q.get()
                s.add(cn)
                self.visit(cn)
                for adj in cn.adjacent:
                    if adj not in s:
                        q.put(adj)

    def breadthFirstSearch(self):
        s = set()
        for key, node in self.nodes.items():
            if node not in s:
                self.bfs(node, s)


def main():

    n, e = map(int, f.readline().split())

    g = Graph()
    nodes = map(int, f.readline().split())

    for _node in nodes:
        g.nodes[_node] = Node(_node)

    for _e in range(e):
        s, d = map(int, f.readline().split())
        g.addEdge(s, d)

    for key, node in g.nodes.items():
        o.write (str(key) + ': ')
        for adj in node.adjacent:
            o.write (str(adj.data) + ' ')
        o.write('\n')

    g.breadthFirstSearch()

if __name__ == "__main__":
    main()

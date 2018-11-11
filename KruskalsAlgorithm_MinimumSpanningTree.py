import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Edge:
    def __init__(self, src, dest, wt):
        self.src, self.dest, self.wt = src, dest, wt

    def __lt__(self, other):
        return self.wt < other.wt

def compute(l, vct):
    l.sort()
    s = {}
    for i in range(1, vct + 1):
        _s = set()
        _s.add(i)
        s[i] = _s
    cost = 0
    for e in l:
        if s[e.src] != s[e.dest]:
            cost += e.wt
            s[e.src] = s[e.src].union(s[e.dest])
            s[e.dest] = s[e.src]
    return cost

def main():
    vct, ne = map(int, f.readline().split())
    l = []
    for e in range(ne):
        src, dest, wt = map(int, f.readline().split())
        l.append(Edge(src, dest, wt))

    print (compute(l, vct))

if __name__ == "__main__":
    main()

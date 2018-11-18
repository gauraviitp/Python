import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class disjointSet:
    def __init__(self, n):
        self.l = [-1] * n

    def find(self, k):
        if self.l[k] != -1:
            self.l[k] = self.find(self.l[k])
            return self.l[k]
        else:
            return k

    def union(self, a, b):
        sa = self.find(a)
        sb = self.find(b)
        self.l[sa] = sb

    def sameSet(self, a, b):
        return self.find(a) == self.find(b)

def main():
    n, m = map(int, f.readline().split())
    d = {}
    for i in range(1, n + 1):
        d[i] = []
    for i in range(m):
        u, v = map(int, f.readline().split())
        d[u].append(v)

    set = disjointSet(n + 1)
    isTree = True
    for u in d.keys():
        for v in d[u]:
            if not set.sameSet(u, v):
                set.union(u, v)
            else:
                isTree = False

    edges = 0
    for i in d.keys():
        edges += len(d[i])

    res = (edges == n - 1) & isTree

    if res:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()

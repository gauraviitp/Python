import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

minVal = int(-1e10)

class Node:
    def __init__(self):
        self.max = minVal
        self.prefix = minVal
        self.suffix = minVal
        self.sum = minVal
        self.val = 0


class SegmentTree:
    def __init__(self, seq):
        self.seq = seq
        h = math.ceil(math.log(len(seq), 2)) + 1
        self.n = len(seq)
        self.nodes = int(math.pow(2, h) - 1)
        self.tree = [Node() for i in range(self.nodes)]
        self.createSegmentTree(0, len(seq) - 1, 0)

    def createSegmentTree(self, lo, hi, ti):
        if lo == hi:
            curNode = self.tree[ti]
            curNode.max = self.seq[lo]
            curNode.prefix = self.seq[lo] if self.seq[lo] < 0 else 0
            curNode.suffix = self.seq[lo] if self.seq[lo] < 0 else 0
            curNode.sum = self.seq[lo]
            curNode.val = self.seq[lo]
            return curNode

        mid = (lo + hi) // 2
        left = self.createSegmentTree(lo, mid, 2 * ti + 1)
        right = self.createSegmentTree(mid + 1, hi, 2 * ti + 2)

        curNode = self.tree[ti]
        curNode.sum = left.sum + right.sum
        curNode.prefix = max(left.sum, left.prefix + left.suffix, left.suffix)
        curNode.suffix = max(right.sum, right.prefix + right.suffix, right.prefix)
        curNode.max = max(left.max, right.max, curNode.prefix, curNode.suffix, curNode.prefix + curNode.suffix)
        return curNode

    def search(self, ss, se, qs, qe, ti):
        if qs <= ss and qe >= se:
            return self.tree[ti]
        if se < qs or ss > qe:
            return Node()

        mid = (ss + se) // 2
        left = self.search(ss, mid, qs, qe, 2 * ti + 1)
        right = self.search(mid + 1, se, qs, qe, 2 * ti + 2)

        curNode = Node()
        curNode.sum = left.sum + right.sum
        curNode.prefix = max(left.sum, left.prefix + left.suffix, left.suffix)
        curNode.suffix = max(right.sum, right.prefix + right.suffix, right.prefix)
        curNode.max = max(left.max, right.max, curNode.prefix, curNode.suffix, curNode.prefix + curNode.suffix)
        return curNode

    def searchTree(self, qs, qe):
        res = self.search(0, self.n - 1, qs, qe, 0)
        return res.max

def main():
    n = int(f.readline())

    h = math.ceil(math.log(n, 2)) + 1
    nodes = int(math.pow(2, h) - 1)

    l = list(map(int, f.readline().split()))
    st = SegmentTree(l)

    m = int(f.readline())
    for _m in range(m):
        a, b = map(int, f.readline().split())
        print(st.searchTree(a - 1, b - 1))

if __name__ == "__main__":
    main()

import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class MaxHeapInt(int):
    def __lt__(self, other):
        return self > other

def solve(li, k):
    n = len(li)
    q = []
    for i in range(k - 1):
        heapq.heappush(q, [MaxHeapInt(li[i]), i])
    for i in range(k - 1, n):
        heapq.heappush(q, [MaxHeapInt(li[i]), i])
        while len(q) > 0 and q[0][1] < (i - (k - 1)):
            heapq.heappop(q)
        yield q[0][0]

def main():
    n = int(f.readline())
    li = list(map(int, f.readline().split()))
    k = int(f.readline())
    for e in solve(li, k):
        o.write(str(e) + ' ')

if __name__ == "__main__":
    main()

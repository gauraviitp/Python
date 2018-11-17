import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Dict(dict):
    def maxKey(self):
        k = 0
        for _k in self.keys():
            k = max(k, _k)
        return k

def solve(n, k):
    d = Dict()
    d[n] = 1
    while True:
        n = d.maxKey()
        cn = d[n]
        if n == 0:
            return [0, 0]
        x0 = (n - 1) // 2
        x1 = (n - 1) // 2 + ((n - 1) % 2 > 0)
        k -= cn
        if k <= 0:
            return [x1, x0]
        if x0 in d:
            d[x0] += cn
        else:
            d[x0] = cn
        if x1 in d:
            d[x1] += cn
        else:
            d[x1] = cn
        d.pop(n)


def main():
    t = int(f.readline())
    for _t in range(1, t + 1):
        n, k = map(int, f.readline().split())
        res = solve(n, k)
        print ('Case #%d: %d %d' % (_t, res[0], res[1]))

if __name__ == "__main__":
    main()

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def possible(x, c, dist):
    pos = x[0]
    for i in range(1, len(x)):
        if c == 0:
            return True
        if x[i] - pos >= dist:
            pos = x[i]
            c -= 1
    if c == 0:
        return True
    return False

def solve(x, c):
    n = len(x)
    lo, hi = x[0], x[n - 1]
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(x, c - 1, mid):
            best = max(mid, best)
            lo = mid + 1
        else:
            hi = mid - 1
    return best

def main():
    t = int(f.readline())
    for _t in range(t):
        n, c = map(int, f.readline().split())
        x = []
        for i in range(n):
            x.append(int(f.readline()))
        x.sort()
        print(solve(x, c))


if __name__ == "__main__":
    main()
